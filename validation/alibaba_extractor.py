#!/usr/bin/env python3
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
import itertools
import pathlib
import pickle

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from slambuc.generator.io import load_hist_params
from slambuc.generator.microservice.faas_tree import DATA_HIST_NAME, RATE_HIST_NAME

MS_CALL_GRAPH_COLS = ("traceid", "rpcid", "um", "rpctype", "dm", "interface", "rt")
NA_VALS = ("NAN", "(?)")
DUP_COLS = ['traceid', 'rpcid', 'rpctype', 'interface']
UNIQUE_CALL_COLS = ['traceid', 'dm', 'interface']
# Attributes of histogram generation
RATE_BIN_CALC_METHOD = 'doane'  # Suitable for large skewed dataset
DATA_BIN_CALC_METHOD = 'doane'  # Suitable for large skewed dataset
DENSITY = True  # Calculate the empirical density function
RATE_RANGE = (1, 100)  # Reduce viable invocation range
DATA_RANGE = (1, 1000)  # Reduce viable data overhead range to be comparable in magnitude with function runtimes


def extract_inv_rate_from_file(file_name: str | pathlib.Path, cache: bool = False) -> list[int]:
    """Extract invocation rates of function wrt. one (Alibaba) call graph in file *file_name*"""
    # Read data file
    print(">> Read data from:", file_name)
    df = pd.read_csv(file_name, header=0, usecols=MS_CALL_GRAPH_COLS, engine='c', na_values=NA_VALS)
    print(">> Filter out invocation calls...")
    # Filter out calls related to stateful services (Database, Memcached)
    # mq/userDefined calls do not contain specific interface -> sub-services in a microservice cannot be differentiated
    df = df[df.rpctype.isin(['http', 'rpc'])]
    # Sanitize data
    df.dropna(subset=['dm'], inplace=True)
    # Filter out duplicate calls recorded also for the backward direction
    df.drop_duplicates(DUP_COLS, inplace=True)
    # Calculate invocations
    inv_calls = df[['rpcid', *UNIQUE_CALL_COLS]].groupby(UNIQUE_CALL_COLS)['rpcid'].count()
    print(f">>>> Found {len(inv_calls)} unique invocation rate value")
    print(inv_calls.describe())
    inv_calls = inv_calls.to_list()
    if cache:
        cache_file = pathlib.Path(pathlib.Path(file_name).stem + "_rate").with_suffix('.npy')
        with open(cache_file, 'wb') as f:
            print(">>>> Dump inv. rate data into", f.name)
            # noinspection PyTypeChecker
            np.save(f, inv_calls, allow_pickle=False)
    return inv_calls


def extract_inv_rate_hist(csv_dir: str, use_cache: bool = True):
    """Extract invocation data from all .csv files and calculate histogram attributes."""
    sum_inv_data = []
    try:
        csv_dir = pathlib.Path(csv_dir).resolve()
        print(f" Iterate over .csv files in {csv_dir} ".center(100, '#'))
        for data_file in csv_dir.glob("MSCallGraph_[0-9]*.csv"):
            cache_file = pathlib.Path(pathlib.Path(data_file).stem + "_rate").with_suffix('.npy')
            if use_cache and cache_file.exists():
                with open(cache_file, 'rb') as f:
                    print("Load inv data from cache", f.name)
                    sum_inv_data.append(np.load(f))
            else:
                sum_inv_data.append(extract_inv_rate_from_file(data_file, cache=use_cache))
    except KeyboardInterrupt:
        pass
    print("Assemble extracted inv data...")
    sum_inv_data = list(itertools.chain.from_iterable(sum_inv_data))
    print("Collected data size", len(sum_inv_data))
    print("Create histogram...")
    inv_hist = np.histogram(sum_inv_data, bins=RATE_BIN_CALC_METHOD, range=RATE_RANGE, density=DENSITY)
    with open(f"{RATE_HIST_NAME}.pkl", 'wb') as f:
        print("Dump hist params into:", f.name)
        # noinspection PyTypeChecker
        pickle.dump(inv_hist, f, protocol=5, fix_imports=True)


########################################################################################################################


def extract_rw_overhead_from_file(file_name: str | pathlib.Path, cache: bool = False) -> list[int]:
    """Extract R/W data overheads wrt. one (Alibaba) call graph in file *file_name*"""
    # Read data file
    print(">> Read data from:", file_name)
    df = pd.read_csv(file_name, header=0, usecols=MS_CALL_GRAPH_COLS, engine='c')
    print(">> Filter out Memcached overheads...")
    # Keep calls related to stateful in-memory app (Memcached)
    df = df[df.rpctype.isin(['mc'])]
    # Sanitize data
    data_rw = df[df.rt > 0]['rt']
    print(f">>>> Found {len(data_rw)} unique data R/W value")
    print(data_rw.describe())
    data_rw = data_rw.to_list()
    if cache:
        cache_file = pathlib.Path(pathlib.Path(file_name).stem + "_data").with_suffix('.npy')
        with open(cache_file, 'wb') as f:
            print(">>>> Dump R/W overhead data into", f.name)
            # noinspection PyTypeChecker
            np.save(f, data_rw, allow_pickle=False)
    return data_rw


def extract_rw_overhead_hist(csv_dir: str, use_cache: bool = True):
    """Extract invocation data from all .csv files and calculate histogram attributes."""
    sum_rw_data = []
    try:
        csv_dir = pathlib.Path(csv_dir).resolve()
        print(f" Iterate over .csv files in {csv_dir} ".center(100, '#'))
        for data_file in csv_dir.glob("MSCallGraph_[0-9]*.csv"):
            cache_file = pathlib.Path(pathlib.Path(data_file).stem + "_data").with_suffix('.npy')
            if use_cache and cache_file.exists():
                with open(cache_file, 'rb') as f:
                    print("Load R/W overhead data from cache", f.name)
                    sum_rw_data.append(np.load(f))
            else:
                sum_rw_data.append(extract_rw_overhead_from_file(data_file, cache=use_cache))
    except KeyboardInterrupt:
        pass
    print("Assemble extracted R/W data...")
    sum_rw_data = list(itertools.chain.from_iterable(sum_rw_data))
    print("Collected data size", len(sum_rw_data))
    print("Create histogram...")
    inv_hist = np.histogram(sum_rw_data, bins=DATA_BIN_CALC_METHOD, range=DATA_RANGE, density=DENSITY)
    with open(f"{DATA_HIST_NAME}.pkl", 'wb') as f:
        print("Dump hist params into:", f.name)
        # noinspection PyTypeChecker
        pickle.dump(inv_hist, f, protocol=5, fix_imports=True)


########################################################################################################################


def extract_all_call_params(csv_dir: str, use_cache: bool = True):
    """Combined invocation rate and R/W data extraction for faster trace processing"""
    sum_inv_data, sum_rw_data = [], []
    try:
        csv_dir = pathlib.Path(csv_dir).resolve()
        print(f" Iterate over .csv files in {csv_dir} ".center(100, '#'))
        for data_file in csv_dir.glob("MSCallGraph_[0-9]*.csv"):
            # Collect inv rate data
            rate_cache_file = pathlib.Path(pathlib.Path(data_file).stem + "_rate").with_suffix('.npy')
            if use_cache and rate_cache_file.exists():
                with open(rate_cache_file, 'rb') as f:
                    print("Load inv data from cache", f.name)
                    sum_inv_data.append(np.load(f))
            else:
                sum_inv_data.append(extract_inv_rate_from_file(data_file, cache=use_cache))
            # Collect R/W data
            data_cache_file = pathlib.Path(pathlib.Path(data_file).stem + "_data").with_suffix('.npy')
            if use_cache and data_cache_file.exists():
                with open(data_cache_file, 'rb') as f:
                    print("Load R/W overhead data from cache", f.name)
                    sum_rw_data.append(np.load(f))
            else:
                sum_rw_data.append(extract_rw_overhead_from_file(data_file, cache=use_cache))
    except KeyboardInterrupt:
        pass
    if not (sum_inv_data and sum_rw_data):
        print("No data are collected!")
        return
    print("Assemble inv. data...")
    sum_inv_data = list(itertools.chain.from_iterable(sum_inv_data))
    print("Collected inv rate data size", len(sum_inv_data))
    print(pd.Series(sum_inv_data).describe())
    if use_cache and not pathlib.Path(f"{RATE_HIST_NAME}.npy").exists():
        with open(f"{RATE_HIST_NAME}.npy", 'wb') as f:
            print(">>>> Dump inv. rate data into", f.name)
            # noinspection PyTypeChecker
            np.save(f, sum_inv_data, allow_pickle=False)
    print("Create inv. rate histograms...")
    inv_hist = np.histogram(sum_inv_data, bins=RATE_BIN_CALC_METHOD, range=RATE_RANGE, density=DENSITY)
    with open(f"{RATE_HIST_NAME}.pkl", 'wb') as f:
        print("Dump rate hist params into:", f.name)
        # noinspection PyTypeChecker
        pickle.dump(inv_hist, f, protocol=5, fix_imports=True)
    print("Assemble R/W data...")
    sum_rw_data = list(itertools.chain.from_iterable(sum_rw_data))
    print("Collected R/W data size", len(sum_rw_data))
    print(pd.Series(sum_rw_data).describe())
    if use_cache and not pathlib.Path(f"{DATA_HIST_NAME}.npy").exists():
        with open(f"{DATA_HIST_NAME}.npy", 'wb') as f:
            print(">>>> Dump R/W data into", f.name)
            # noinspection PyTypeChecker
            np.save(f, sum_inv_data, allow_pickle=False)
    print("Create R/W data histograms...")
    data_hist = np.histogram(sum_rw_data, bins=DATA_BIN_CALC_METHOD, range=DATA_RANGE, density=DENSITY)
    with open(f"{DATA_HIST_NAME}.pkl", 'wb') as f:
        print("Dump R/W hist params into:", f.name)
        # noinspection PyTypeChecker
        pickle.dump(data_hist, f, protocol=5, fix_imports=True)


def extract_all_call_params_from_cache(cache_dir: str):
    """Combined invocation rate and R/W data extraction for faster trace processing"""
    sum_inv_data, sum_rw_data = [], []
    try:
        csv_dir = pathlib.Path(cache_dir).resolve()
        print(f"Iterate over .npy files in {csv_dir} ".center(100, '#'))
        for i in range(1, 145):
            # Collect inv rate data
            rate_cache_file = pathlib.Path(pathlib.Path(f"MSCallGraph_{i}").stem + "_rate").with_suffix('.npy')
            if rate_cache_file.exists():
                with open(rate_cache_file, 'rb') as f:
                    print("Load inv data from cache", f.name)
                    sum_inv_data.append(np.load(f))
            else:
                print(f">>>> Cache file: {rate_cache_file} is missing!")
            # Collect R/W data
            data_cache_file = pathlib.Path(pathlib.Path(f"MSCallGraph_{i}").stem + "_data").with_suffix('.npy')
            if data_cache_file.exists():
                with open(data_cache_file, 'rb') as f:
                    print("Load R/W overhead data from cache", f.name)
                    sum_rw_data.append(np.load(f))
            else:
                print(f">>>> Cache file: {data_cache_file} is missing!")
    except KeyboardInterrupt:
        pass
    if not (sum_inv_data and sum_rw_data):
        print("No data are collected!")
        return
    print("Assemble inv. data...")
    sum_inv_data = list(itertools.chain.from_iterable(sum_inv_data))
    print("Collected inv rate data size", len(sum_inv_data))
    print(pd.Series(sum_inv_data).describe())
    if not pathlib.Path(f"{RATE_HIST_NAME}.npy").exists():
        with open(f"{RATE_HIST_NAME}.npy", 'wb') as f:
            print(">>>> Dump inv. rate data into", f.name)
            # noinspection PyTypeChecker
            np.save(f, sum_inv_data, allow_pickle=False)
    print("Create inv. rate histograms...")
    inv_hist = np.histogram(sum_inv_data, bins=RATE_BIN_CALC_METHOD, range=RATE_RANGE, density=DENSITY)
    with open(f"{RATE_HIST_NAME}.pkl", 'wb') as f:
        print("Dump rate hist params into:", f.name)
        # noinspection PyTypeChecker
        pickle.dump(inv_hist, f, protocol=5, fix_imports=True)
    print("Assemble R/W data...")
    sum_rw_data = list(itertools.chain.from_iterable(sum_rw_data))
    print("Collected R/W data size", len(sum_rw_data))
    print(pd.Series(sum_rw_data).describe())
    if not pathlib.Path(f"{DATA_HIST_NAME}.npy").exists():
        with open(f"{DATA_HIST_NAME}.npy", 'wb') as f:
            print(">>>> Dump R/W data into", f.name)
            # noinspection PyTypeChecker
            np.save(f, sum_inv_data, allow_pickle=False)
    print("Create R/W data histograms...")
    data_hist = np.histogram(sum_rw_data, bins=DATA_BIN_CALC_METHOD, range=DATA_RANGE, density=DENSITY)
    with open(f"{DATA_HIST_NAME}.pkl", 'wb') as f:
        print("Dump R/W hist params into:", f.name)
        # noinspection PyTypeChecker
        pickle.dump(data_hist, f, protocol=5, fix_imports=True)


def plot_hists(hist_name: str):
    plt.figure(figsize=(10, 5))
    hist_params = load_hist_params("../slambuc/generator/microservice/hist", hist_name)
    plt.stairs(*hist_params, fill=True)
    plt.yscale('log')
    plt.grid(linestyle='dotted', zorder=0)
    plt.title(hist_name)
    plt.show()
    plt.close()


if __name__ == '__main__':
    # extract_inv_rate_hist(".")
    # extract_rw_overhead_hist('.')
    extract_all_call_params('.')
    #
    # plot_hists(RATE_HIST_NAME)
    # plot_hists(DATA_HIST_NAME)
