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
import collections
import os
import pathlib
import re
import shutil

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def merge_results(dir1="../results/perf/", dir2="/results"):
    def alphaNumOrder(string):
        return ''.join([format(int(x), '03d') if x.isdigit() else x for x in re.split(r'(\d+)', string)])

    for csv_file in sorted(pathlib.Path(dir1).rglob("*.csv")):
        print("Read file:", csv_file)
        df = pd.read_csv(csv_file)
        if (df2_file := pathlib.Path(dir2, csv_file.name)).exists():
            print("Concat file:", df2_file)
            df2 = pd.read_csv(df2_file)
            for alg in df2["Alg"].unique():
                df = df[df.Alg != alg]
            df = pd.concat((df, pd.read_csv(df2_file)), ignore_index=True)
        else:
            print(">>> Missing file:", df2_file)
        df.sort_values(by=["Tree", "Alg"], inplace=True, key=lambda col: [alphaNumOrder(x) for x in col])
        df.reset_index(drop=True, inplace=True)
        df.to_csv(csv_file, mode='w', header=True, index=False)
        print(f"Write sorted file to", csv_file)


def set_pgf_backend(style: str = "ggplot"):
    plt.style.use(style)
    matplotlib.use("pgf")
    matplotlib.rcParams.update(
        {"pgf.texsystem": "pdflatex", 'font.family': 'serif', 'text.usetex': True, 'pgf.rcfonts': False})


def save_to_pgf():
    plt.savefig("example.pgf")


def save_time_bar_pgf(csv_file: str = "../results/perf/test_tree_size_ser_n10.csv", style="classic"):
    set_pgf_backend(style=style)
    df = pd.read_csv(csv_file)
    df.loc[df.Cost == np.inf, "Time"] = 1000.0
    plt.figure(figsize=(12, 5))
    ax = plt.gca()
    df[['Alg', 'Time']].plot.box(by="Alg", ax=ax, showfliers=False)
    plt.grid(linestyle='dotted', zorder=0)
    plt.xlabel('Alg')
    plt.ylabel('Time')
    plt.title(csv_file)
    plt.tight_layout()
    save_to_pgf()


def save_time_bar_pgf_directly(csv_file: str = "../results/perf/test_tree_size_ser_n10.csv", showfliers: bool = True):
    from matplotlib.backends.backend_pgf import FigureCanvasPgf
    matplotlib.backend_bases.register_backend('pdf', FigureCanvasPgf)

    df = pd.read_csv(csv_file)
    df.loc[df.Cost == np.inf, "Time"] = 1000.0
    plt.figure(figsize=(12, 5))
    plt.gcf().set_size_inches(w=3.48761, h=3.48761)
    ax = plt.gca()
    df[['Alg', 'Time']].plot.box(by="Alg", ax=ax, showfliers=showfliers)
    plt.grid(linestyle='dotted', zorder=0)
    plt.xlabel('Alg')
    plt.ylabel('Time')
    plt.title(csv_file)
    plt.tight_layout()
    plt.savefig("example.pdf")


def test_pgf_latex_binding():
    if (pgf := pathlib.Path("example.pgf").resolve()).exists():
        os.remove(pgf)
    if (pdf := pathlib.Path("example2.pdf").resolve()).exists():
        os.remove(pdf)
    shutil.rmtree(pathlib.Path("../../out").resolve(), ignore_errors=True)
    save_time_bar_pgf()
    save_time_bar_pgf_directly(showfliers=False)


########################################################################################################################


def plot_time_bar(csv_file: str = "../results/perf/test_tree_size_ser_n10.csv", showfliers: bool = True):
    df = pd.read_csv(csv_file)
    df.loc[df.Cost == np.inf, "Time"] = 1000.0
    plt.figure(figsize=(12, 5))
    ax = plt.gca()
    df[['Alg', 'Time']].plot.box(by="Alg", ax=ax, showfliers=showfliers)
    plt.grid(linestyle='dotted', zorder=0)
    plt.xlabel('Alg')
    plt.ylabel('Time')
    plt.title(csv_file)
    plt.tight_layout()
    plt.show()


def plot_all_bar(_type: str = "ser", showfliers: bool = False):
    for n in range(10, 101, 10):
        plot_time_bar(f"../results/perf/test_tree_size_{_type}_n{n}.csv", showfliers=showfliers)


def plot_alg_runtimes(alg_type: str = "ser", avg: bool = False):
    results = []
    for n in range(10, 101, 10):
        df = pd.read_csv(f"../results/perf/test_tree_size_{alg_type}_n{n}.csv")
        if avg:
            df.dropna(subset=['Lat'], inplace=True)
            row = df[['Alg', 'Time']].groupby('Alg').mean().transpose()
        else:
            df.loc[df.Cost == np.inf, "Time"] = 1000.0
            row = df[['Alg', 'Time']].groupby('Alg').median().transpose()
        row.set_index(pd.Index([n], dtype=int, name="Tree Size"), inplace=True)
        results.append(row)
    df = pd.concat(results, ignore_index=False)
    plt.figure(figsize=(10, 5))
    ax = plt.gca()
    df.plot(ax=ax, subplots=False, marker='s', fillstyle='none')
    ax.grid(linestyle='dotted', zorder=0)
    ax.set_yscale('log')
    ax.set_xticks(df.index)
    # plt.xlabel('Tree size')
    ax.set_ylabel('Median Runtime [s]' if not avg else 'Mean Runtime [s]')
    ax.set_title(f"{alg_type}")
    plt.tight_layout()
    plt.show()


def plot_sens_tests(n: int = 40, param: str = "m", _ax=None, avg: bool = False):
    results = []
    for csv_file in sorted(pathlib.Path(f"../results/sens/").glob(f"test_alg_sens_n{n}_{param}?.?.csv")):
        df = pd.read_csv(csv_file)
        df.dropna(subset=['Lat'], inplace=True)
        if avg:
            row = df[['Alg', 'Time']].groupby('Alg').mean().transpose()
        else:
            df.loc[df.Cost == np.inf, "Time"] = 1000.0
            row = df[['Alg', 'Time']].groupby('Alg').median().transpose()
        param_value = csv_file.stem.rsplit(sep='_')[-1].lstrip(param)
        row.set_index(pd.Index([param_value], dtype=float, name=f"Param {param}"), inplace=True)
        results.append(row)
    df = pd.concat(results, ignore_index=False)
    if not _ax:
        plt.figure(figsize=(15, 5))
        ax = plt.gca()
    else:
        ax = _ax
    df.plot(ax=ax, subplots=False)
    ax.grid(linestyle='dotted', zorder=0)
    ax.set_yscale('log')
    ax.set_xticks(df.index)
    # plt.xlabel('Tree size')
    ax.set_ylabel('Median Runtime [s]' if not avg else 'Mean Runtime [s]')
    ax.set_title(f"Sens - tree: {n}, param: {param}")
    if not _ax:
        plt.tight_layout()
        plt.show()


def plot_sens_by_tree_size(param: str = "m", avg: bool = False):
    fig = plt.figure(figsize=(24, 8))
    gs = fig.add_gridspec(2, 2)
    axes = gs.subplots(sharex=True, sharey=True)
    # fig.suptitle("")
    for n, ax in zip(range(40, 71, 10), axes.flatten()):
        plot_sens_tests(n, param, _ax=ax, avg=avg)
    plt.tight_layout()
    plt.show()


def plot_sens_bicrit_heatmap(n: int = 40, avg: bool = False):
    results = collections.defaultdict(dict)
    for csv_file in sorted(pathlib.Path(f"../results/sens/").glob(f"test_alg_sens_n{n}_bicrit_*.csv")):
        df = pd.read_csv(csv_file)
        if avg:
            df.dropna(subset=['Lat'], inplace=True)
            t = df[['Alg', 'Time']].groupby('Alg').mean()['Time'][0]
        else:
            df.loc[df.Cost == np.inf, "Time"] = 1000.0
            t = df[['Alg', 'Time']].groupby('Alg').median()['Time'][0]
        eps, lam = map(float, csv_file.stem.rsplit(sep='_')[-1].split('-'))
        results[lam][eps] = t
    # del results[0.0]
    df = pd.DataFrame.from_dict(results, orient='index')
    df.columns.name = "eps"
    df.index.name = "lam"  # x: eps, y: lam
    df.sort_index(inplace=True)
    plt.imshow(df, cmap='gray_r', interpolation='nearest', origin="lower", norm='log')
    # plt.imshow(df, cmap='gray_r', interpolation='nearest', origin="lower", norm=LogNorm(vmin=0.0111, vmax=0.06))
    plt.colorbar()
    plt.xlabel('Epsilon')
    # plt.xticks(df.columns)
    plt.ylabel("Lambda")
    # plt.yticks(df.index)
    plt.title('Median Time')
    plt.tight_layout()
    plt.show()


def plot_cost_time_tests(tree: str = "random", _ax=None):
    results = []
    for csv_file in sorted(pathlib.Path(f"../results/cost/").glob(f"test_alg_cost_{tree}_tree_n*.csv")):
        df = pd.read_csv(csv_file)
        df.loc[df.Cost == np.inf, "Time"] = 1000.0
        row = df[['Alg', 'Time']].groupby('Alg').median().transpose()
        n1, n2 = map(int, csv_file.stem.rsplit(sep='n')[-1].split('-'))
        row.set_index(pd.IntervalIndex.from_tuples([(n1, n2)], dtype="interval[int64, left]'", closed="left",
                                                   name=f"Tree Size"), inplace=True)
        results.append(row)
    df = pd.concat(results, ignore_index=False)
    if not _ax:
        plt.figure(figsize=(15, 5))
        ax = plt.gca()
    else:
        ax = _ax
    df.plot(ax=ax, subplots=False)
    ax.grid(linestyle='dotted', zorder=0)
    ax.set_yscale('log')
    # ax.set_xticks(df.index)
    # plt.xlabel('Tree size')
    ax.set_ylabel('Median Time')
    ax.set_title(f"Cost - {tree} tree")
    if not _ax:
        plt.tight_layout()
        plt.show()


def plot_cost_time_by_tree_type():
    fig = plt.figure(figsize=(20, 5))
    gs = fig.add_gridspec(1, 3)
    axes = gs.subplots(sharex=True, sharey=False)
    # fig.suptitle("")
    for tree, ax in zip(("random", "job", "faas"), axes.flatten()):
        plot_cost_time_tests(tree, _ax=ax)
    plt.tight_layout()
    plt.show()


def plot_cost_profit_test(csv_file: str = "../results/cost/test_alg_cost_job_tree_n10-20.csv", showfliers: bool = True):
    df = pd.read_csv(csv_file)
    df.loc[df.Cost == np.inf, "Time"] = 1000.0
    trees = df.Tree.unique()
    df = df[['Tree', 'Alg', 'Cost']]
    df.set_index(['Tree', 'Alg'], inplace=True)
    for t in trees:
        df.loc[[t]] = (df.loc[[t]] - df.loc[t, "OPT"].Cost) / df.loc[[t]] * 100
    df.reset_index(inplace=True)
    plt.figure(figsize=(15, 5))
    ax = plt.gca()
    df[['Alg', 'Cost']].plot.box(by="Alg", ax=ax, showfliers=showfliers)
    plt.grid(linestyle='dotted', zorder=0)
    plt.xlabel('Alg')
    plt.ylabel('Cost')
    plt.title(csv_file)
    plt.tight_layout()
    plt.show()


def plot_cost_profit_by_tree_size(tree: str = "random", showfliers: bool = True):
    for n in range(10, 91, 10):
        plot_cost_profit_test(f"../results/cost/test_alg_cost_{tree}_tree_n{n}-{n + 10}.csv", showfliers=showfliers)


def plot_cost_lat_scatter(csv_file: str = "../results/cost/test_alg_cost_job_tree_n10-20.csv"):
    df = pd.read_csv(csv_file)
    df.loc[df.Cost == np.inf, "Time"] = 1000.0
    trees = df.Tree.unique()
    df2 = df[['Tree', 'Alg', 'Cost']]
    df2 = df2.set_index(['Tree', 'Alg'])
    for t in trees:
        df2.loc[[t]] = (df2.loc[[t]] - df2.loc[t, "OPT"].Cost) / df2.loc[[t]] * 100
    df2.reset_index(inplace=True)
    df2['Lat'] = (df['Lat'] - df['L']) / df['L'] * 100
    # df2 = df2[df2.Alg != "OPT"]
    fig = plt.figure(figsize=(24, 8))
    gs = fig.add_gridspec(2, 5)
    axes = gs.subplots(sharex=True, sharey=True)
    for alg, ax in zip(df2.Alg.unique(), axes.flatten()):
        ax.axhline(0, color='black')
        ax.axvline(0, color='black')
        df2[df2.Alg == alg][['Cost', 'Lat']].plot.scatter(x="Cost", y="Lat", ax=ax)
        ax.grid(linestyle='dotted', zorder=0)
        ax.set_title(alg)
        # ax.set_xlabel('Cost')
        # ax.set_ylabel('Lat')
    fig.suptitle(csv_file)
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    # merge_results("../results/perf/", "../results/")
    # merge_results("../results/sens/", "../results/")
    # merge_results("../results/cost/", "../results/")
    #
    #
    # plot_time_bar("../results/perf/test_tree_size_ser_n10.csv", showfliers=False)
    # plot_time_bar("../results/perf/test_tree_size_par_n30.csv")
    #
    # plot_all_bar(_type="ser")
    # plot_all_bar(_type="par")
    #
    # plot_sens_tests(n=40, param="m")
    # plot_sens_tests(n=40, param="l")
    # plot_sens_tests(n=40, param="cpu")
    #
    #
    # plot_sens_tests(n=40, param="eps")
    # plot_sens_tests(n=40, param="lam")
    #
    # plot_sens_by_tree_size(param="eps")
    # plot_sens_by_tree_size(param="lam")
    #
    # plot_sens_bicrit_heatmap(n=10)
    # plot_sens_bicrit_heatmap(n=20)
    # plot_sens_bicrit_heatmap(n=30)
    # plot_sens_bicrit_heatmap(n=40)
    # plot_sens_bicrit_heatmap(n=50)
    # plot_sens_bicrit_heatmap(n=30, avg=True)
    #
    # plot_cost_time_tests(tree="random")
    # plot_cost_time_tests(tree="job")
    # plot_cost_time_tests(tree="faas")
    #
    # plot_cost_time_by_tree_type()
    #
    # plot_cost_profit_test(csv_file= "../results/cost/test_alg_cost_job_tree_n10-20.csv")
    # plot_cost_profit_test(csv_file= "../results/cost/test_alg_cost_job_tree_n30-40.csv")
    # plot_cost_profit_by_tree_size(tree="random")
    # plot_cost_profit_by_tree_size(tree="job")
    # plot_cost_profit_by_tree_size(tree="faas")
    #
    # plot_cost_lat_scatter(csv_file="../results/cost/test_alg_cost_job_tree_n10-20.csv")
    # plot_cost_lat_scatter(csv_file="../results/cost/test_alg_cost_faas_tree_n10-20.csv")
    # plot_cost_lat_scatter(csv_file="../results/cost/test_alg_cost_faas_tree_n40-50.csv")
    # plot_cost_lat_scatter(csv_file="../results/cost/test_alg_cost_job_tree_n40-50.csv")
    #
    #
    # save_time_bar_pgf(style="classic")
    # save_time_bar_pgf_directly()
    # test_pgf_latex_binding()
    #############
    # plot_alg_runtimes(alg_type="ser")
    # plot_alg_runtimes(alg_type="ser", avg=True)
    # plot_alg_runtimes(alg_type="par")
    # plot_alg_runtimes(alg_type="par", avg=True)
    #############
    # plot_sens_by_tree_size(param="m")
    # plot_sens_by_tree_size(param="m", avg=True)
    # plot_sens_by_tree_size(param="l")
    # plot_sens_by_tree_size(param="l", avg=True)
    # plot_sens_by_tree_size(param="cpu")
    # plot_sens_by_tree_size(param="cpu", avg=True)
    #############
    # plot_sens_bicrit_heatmap(n=40, avg=False)
    #############
    plot_cost_time_by_tree_type()
    #############
