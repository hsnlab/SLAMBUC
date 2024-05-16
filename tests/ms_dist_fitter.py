#!/usr/bin/env python3.11
import pathlib
import pickle

import fitter
import numpy as np
import scipy

DISTS = ['burr', 'burr12', 'alpha', 'beta', 'expon', 'lognorm',
         'gamma', 'norm', 'powerlaw', 'exponpow', 'exponnorm', 'logistic']
SIZE = 100_000
BINS = 1000

RATE_HIST_NAME = "func_inv_rate_hist"
DATA_HIST_NAME = "rw_overhead_hist"


def load_emp_hist(name):
    with open(f"../slambuc/gen/microservice/hist/{name}.pkl", 'rb') as f:
        return pickle.load(f, fix_imports=True)


########################################################################################################################


def get_inv_distribution():
    print(RATE_HIST_NAME)
    if pathlib.Path(f"hist/{RATE_HIST_NAME}.npy").exists():
        with open(f"hist/{RATE_HIST_NAME}.npy", 'rb') as f:
            print(">>>> Load inv. rate data from", f.name)
            rate_data = np.load(f)
    else:
        rate_hist = scipy.stats.rv_histogram(load_emp_hist(RATE_HIST_NAME), density=True)
        print("histogram:", rate_hist)

        rate_data = rate_hist.rvs(size=SIZE)
    print("Data size", len(rate_data))
    fit = fitter.Fitter(data=rate_data, bins=BINS, distributions=DISTS, timeout=600, density=True)
    print("fitter:", fit)
    fit.fit(progress=True)
    print(fit.summary(Nbest=len(DISTS)))
    print(fit.get_best())


def get_rw_distribution():
    print(DATA_HIST_NAME)
    if pathlib.Path(f"hist/{DATA_HIST_NAME}.npy").exists():
        with open(f"hist/{DATA_HIST_NAME}.npy", 'rb') as f:
            print(">>>> Load R/W data from", f.name)
            data_data = np.load(f)
    else:
        data_hist = scipy.stats.rv_histogram(load_emp_hist(DATA_HIST_NAME), density=True)
        print("histogram:", data_hist)

        data_data = data_hist.rvs(size=SIZE)
    print("Data size", len(data_data))
    fit = fitter.Fitter(data=data_data, bins=BINS, distributions=DISTS, timeout=600, density=True)
    print("fitter:", fit)
    fit.fit(progress=True)
    print(fit.summary(Nbest=len(DISTS)))
    print(fit.get_best())


if __name__ == '__main__':
    get_inv_distribution()
    get_rw_distribution()
