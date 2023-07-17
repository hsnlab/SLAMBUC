# Copyright 2023 Janos Czentye
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at:
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import functools
import logging
import math
import multiprocessing
import os
import pathlib
import resource
import signal
import time

import psutil

PAGESIZE = resource.getpagesize()


def get_total_memory(unit_exp: int = 2) -> int:
    """
    Return the total available memory in given *unit_exp* (0 -> bytes, 1 -> KB, 2 -> MB, 3 -> GB, ...).
    """
    # return int(os.popen(f"free -t -{unit}").readlines()[1].split()[1])
    return psutil.virtual_memory().total / 1024 ** unit_exp


def check_total_used_memory(unit_exp: int = 2) -> int:
    """
    Return the total used memory in given *unit_exp* (0 -> bytes, 1 -> KB, 2 -> MB, 3 -> GB, ...).
    """
    # return int(os.popen(f"free -t -{unit}").readlines()[1].split()[2])
    # return psutil.virtual_memory().used / 1024 ** unit_exp
    mem = psutil.virtual_memory()
    return (mem.total - mem.free) / 1024 ** unit_exp


def check_process_memory(pid: int | str = 'self', unit_exp: int = 2) -> float:
    """
    Return the memory usage of a process given by the *PID* with units based on the given *unit_exp*
    (0 -> bytes, 1 -> KB, 2 -> MB, 3 -> GB, ...).

    See also: https://stackoverflow.com/a/53475728
    """
    try:
        # rss = psutil.Process(None if pid == "self" else pid).memory_full_info().rss
        rss = int(pathlib.Path(f"/proc/{pid}/statm").read_text().split(' ', maxsplit=2)[1]) * PAGESIZE
    except FileNotFoundError:
        return None
    return rss / 1024 ** unit_exp


class TestGovernor(multiprocessing.Process):
    """
    Watch the given process and send aort signal in case of exceeded memory limit.
    """
    DEF_SLEEP: int = 3
    BACKOFF_WINDOW: int = DEF_SLEEP * 4
    LOG_FILE: str = "governor.log"
    DEF_LOG_LEVEL: int = logging.DEBUG

    def __init__(self, pid: int = None, target: int = None, mem_limit: int | float = 0.95, time_limit: int = None,
                 interval: int = DEF_SLEEP, log_level: str = DEF_LOG_LEVEL):
        """
        Initialize test governor as a separate subprocess.

        :param pid:         PID of the monitored process (default: all processes)
        :param target:      PID of the governed process (default: own process)
        :param mem_limit:   memory limit in MB (default: 95% of total available memory)
        :param time_limit:  overall timeout limit in sec (default: no limit)
        :param interval:    check interval in sec (default: 3)
        :param log_level:   enable file logging (default: False)
        """
        if pid is None:
            self.__pid, self.check_mem = "*", check_total_used_memory
        else:
            self.__pid, self.check_mem = pid, functools.partial(check_process_memory, pid=pid)
        self.__target = target if target else os.getpid()
        self.__mlimit = math.ceil(mem_limit * get_total_memory()) if 0 < mem_limit < 1 else mem_limit
        self.__tlimit = time_limit
        self.__tstart = None
        self.__last_signal = time.time()
        self.interval = interval
        self.set_logger(log_level)
        super().__init__(target=self.watch, name=self.__class__, daemon=True)
        self.log.info(self)

    @property
    def mlimit(self):
        return self.__mlimit

    @property
    def tlimit(self):
        return self.__mlimit

    def __str__(self):
        return (f"{self.__class__.__name__} watching PID [{self.__pid}] for target: {self.__target} with"
                f" runtime limits: [{self.__mlimit} MB, {self.__tlimit} s], interval: {self.interval} s, "
                f"backoff: {self.BACKOFF_WINDOW} s")

    def set_logger(self, log_level):
        """Set up logging into file."""
        self.log = logging.getLogger(self.__class__.__name__)
        self.log.setLevel(log_level)
        fh = logging.FileHandler(self.LOG_FILE, mode='w')
        fh.setFormatter(logging.Formatter("[%(asctime)s][%(name)s][%(levelname)s]: %(message)s"))
        self.log.handlers = [fh]

    def clear_timer(self):
        """Clear overall test execution timer."""
        self.__tstart = time.time()

    def start(self):
        """Start measuring overall test time and initiate TestGovernor as a subprocess."""
        self.log.info(f"Start watching process with PID [{self.__pid}] for target process: {self.__target}")
        self.__tstart = time.time()
        super().start()

    def run(self):
        """Implicitly close resources in case of interrupted tests."""
        try:
            self.log.debug(f"{self.__class__.__name__} subprocess initiated with pid: {self.pid}")
            super().run()
        except KeyboardInterrupt:
            self.close()

    def watch(self):
        """Start watching given process or all used memory and send specific signal in case of limit violation."""
        while True:
            delta = time.time() - self.__tstart
            if (mem := self.check_mem()) is None:
                self.log.info(f"Target process {self.__target} does not exist or terminated!")
                break
            elif mem >= self.__mlimit:
                if abs(time.time() - self.__last_signal) <= self.BACKOFF_WINDOW:
                    self.log.debug(f"PID: {self.__pid}, mem: {mem:.2f} MB exceeded limit {self.__mlimit} MB"
                                   f" -> retain ABORT signal due to backoff window [{self.BACKOFF_WINDOW} s]")
                else:
                    os.kill(self.__target, signal.SIGABRT)
                    self.__last_signal = time.time()
                    self.log.warning(f"PID: {self.__pid}, mem: {mem:.2f} MB exceeded limit {self.__mlimit} MB"
                                     f" -> sent ABORT signal to process: {self.__target}")
            elif self.__tlimit and delta > self.__tlimit:
                os.kill(self.__target, signal.SIGALRM)
                self.__last_signal = time.time()
                self.log.warning(f"PID: {self.__pid}, time: {delta:.2f} s exceeded limit {self.__tlimit} s"
                                 f" -> sent ALERT signal to process: {self.__target}")
                self.clear_timer()
            else:
                self.log.debug(f"PID: {self.__pid}, mem: {mem:.2f} MB, time: {delta:.2f} s")
            time.sleep(self.DEF_SLEEP)

    def close(self):
        """Close all used resources."""
        self.log.info(f"End watching process with PID [{self.__pid}] for target process: {self.__target}")
        super().close()

    def shutdown(self):
        """Shutdown."""
        if self.is_alive():
            self.terminate()
            self.join()
        self.close()


if __name__ == '__main__':
    # tg = TestGovernor(os.getpid())
    tg = TestGovernor()
    tg.start()
    time.sleep(4)
    tg.shutdown()
