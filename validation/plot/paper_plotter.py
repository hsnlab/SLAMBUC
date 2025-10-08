# Copyright 2025 Janos Czentye
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
import itertools
import pathlib

import matplotlib
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import ticker as mticker
from matplotlib.backends.backend_pgf import FigureCanvasPgf

from slambuc.alg.util import isubtrees, ser_subtree_memory
from slambuc.misc.io import get_tree_from_file

matplotlib.backend_bases.register_backend('pdf', FigureCanvasPgf)
matplotlib.rcParams.update({"pgf.texsystem": "pdflatex",
                            # 'font.family': 'serif',
                            'text.usetex': False,
                            'pgf.rcfonts': False})
# matplotlib.use("pgf")

PALGS = dict(ILP_HYBRID=r"CfgILP", ILP_HYBRID_PAR=r"CfgILP", ILP_MTX=r"MtxILP", ILP_MTX_PAR=r"MtxILP", PSEUDO_B=r"BUTP",
             PSEUDO_B_BI=r"BUTP+BI", PSEUDO_B_MP=r"BUTP+MP", PSEUDO_L=r"LRTP", PSEUDO_L_PAR=r"LRTP",
             PSEUDO_L_BI=r"LRTP+BI", PSEUDO_L_PAR_BI=r"LRTP+BI", PSEUDO_L_MP=r"LRTP+MP", PSEUDO_L_PAR_MP=r"LRTP+MP",
             BIFPTAS_L=r"BiFPTAS", GREEDY=r"GrTP")

PSTYLES = dict(ILP_HYBRID="-", ILP_HYBRID_PAR="-", ILP_MTX="-", ILP_MTX_PAR="-", PSEUDO_B=":", PSEUDO_B_BI=":",
               PSEUDO_B_MP=":", PSEUDO_L=":", PSEUDO_L_BI=":", PSEUDO_L_MP=":", PSEUDO_L_PAR=":", PSEUDO_L_PAR_BI=":",
               PSEUDO_L_PAR_MP=":", BIFPTAS_L="--", GREEDY="-.")

PCOLOR = dict(ILP_HYBRID="g", ILP_MTX="g", ILP_HYBRID_PAR="g", ILP_MTX_PAR="g", PSEUDO_B="m", PSEUDO_B_BI="m",
              PSEUDO_B_MP="m", PSEUDO_L="k", PSEUDO_L_BI="k", PSEUDO_L_MP="k", PSEUDO_L_PAR="k", PSEUDO_L_PAR_BI="k",
              PSEUDO_L_PAR_MP="k", BIFPTAS_L="b", GREEDY="r")

PMARKER = dict(ILP_HYBRID="o", ILP_MTX="o", ILP_HYBRID_PAR="o", ILP_MTX_PAR="o", PSEUDO_B="s", PSEUDO_B_BI="s",
               PSEUDO_B_MP="s", PSEUDO_L="s", PSEUDO_L_BI="s", PSEUDO_L_MP="s", PSEUDO_L_PAR="s", PSEUDO_L_PAR_BI="s",
               PSEUDO_L_PAR_MP="s", BIFPTAS_L="s", GREEDY="D")

PFILL = dict(ILP_HYBRID="none", ILP_MTX="full", ILP_HYBRID_PAR="none", ILP_MTX_PAR="full", PSEUDO_B="none",
             PSEUDO_B_BI="full", PSEUDO_B_MP="bottom", PSEUDO_L="none", PSEUDO_L_BI="full", PSEUDO_L_MP="top",
             PSEUDO_L_PAR="none", PSEUDO_L_PAR_BI="full", PSEUDO_L_PAR_MP="top", BIFPTAS_L="none", GREEDY="none")

# elsarticle.cls
COLUMN_W = 3.48761  # in
TEXT_W = 7.22433  # in
M_SIZE = 4
LINE_W = 1


def plot_alg_runtimes(alg_type: str = "serial", show: bool = True, ext: str = "pgf"):
    plt.style.use('fast')
    plt.rc('font', size=5)
    plt.rc('axes', labelsize=6)
    plt.rc('legend', fontsize=5)
    plt.figure(figsize=(COLUMN_W, COLUMN_W - 1.7))
    results = []
    for n in range(10, 101, 10):
        df = pd.read_csv(f"../results/perf/test_tree_size_{alg_type}_n{n}.csv")
        # df.loc[df.Cost == np.inf, "Time"] = 1000.0
        df.dropna(subset=['Lat'], inplace=True)
        row = df[['Alg', 'Time']].groupby('Alg').median().transpose()
        # row = df[['Alg', 'Time']].groupby('Alg').mean().transpose()
        row.set_index(pd.Index([n], dtype=int, name="Tree Size"), inplace=True)
        results.append(row)
    df = pd.concat(results, ignore_index=False)
    # df.plot(ax=ax, subplots=False, marker='s', fillstyle='none')
    for alg in PALGS:
        if alg not in df:
            continue
        plt.plot(df[alg], color=PCOLOR[alg], marker=PMARKER[alg], markersize=M_SIZE, fillstyle=PFILL[alg],
                 linewidth=LINE_W, linestyle=PSTYLES[alg], label=PALGS[alg])
    plt.grid(linestyle='dotted', zorder=0)
    plt.xticks(df.index)
    plt.xlabel("Tree size ($n$)")  # ,labelpad=1)
    plt.yticks(rotation=90, ha="center", va="baseline")
    plt.yscale('log')
    plt.ylim(bottom=4e-4, top=2e3)
    plt.ylabel("Median runtime [sec]")  # ,labelpad=1)
    plt.legend(loc="upper left", fancybox=True, framealpha=1, ncol=2, columnspacing=0.5)  # labelspacing=0.5)
    plt.tight_layout(pad=0.3)
    if show:
        plt.show()
    else:
        plt.savefig(f"figs/alg_perf_runtimes_{alg_type}.{ext}")


########################################################################################################################

ALGS = dict(ILP_HYBRID=r"CfgILP", ILP_HYBRID_PAR=r"CfgILP", ILP_MTX=r"MtxILP", ILP_MTX_PAR=r"MtxILP",
            PSEUDO_B=r"BUTP+BI", PSEUDO_L=r"LRTP+BI", PSEUDO_L_PAR=r"LRTP", BIFPTAS_L=r"BiFPTAS", GREEDY=r"GrTP")

STYLES = dict(ILP_HYBRID="-", ILP_HYBRID_PAR="-", ILP_MTX="-", ILP_MTX_PAR="-", PSEUDO_B=":", PSEUDO_L=":",
              PSEUDO_L_PAR=":", BIFPTAS_L="--", GREEDY="-.")

COLOR = dict(ILP_HYBRID="g", ILP_MTX="g", ILP_HYBRID_PAR="g", ILP_MTX_PAR="g", PSEUDO_B="m", PSEUDO_L="k",
             PSEUDO_L_PAR="k", BIFPTAS_L="b", GREEDY="r")

MARKER = dict(ILP_HYBRID="o", ILP_MTX="o", ILP_HYBRID_PAR="o", ILP_MTX_PAR="o", PSEUDO_B="s", PSEUDO_L="s",
              PSEUDO_L_PAR="s", BIFPTAS_L="s", GREEDY="D")

FILL = dict(ILP_HYBRID="none", ILP_MTX="full", ILP_HYBRID_PAR="none", ILP_MTX_PAR="full", PSEUDO_B="full",
            PSEUDO_L="full", PSEUDO_L_PAR="none", BIFPTAS_L="none", GREEDY="none")

# SENS_TREES = (40, 50, 60, 70)
SENS_TREES = (10, 30, 50, 70)


def plot_sens_runtimes(param: str = "m", show: bool = True, ext: str = "pgf"):
    plt.style.use('fast')
    plt.rc('font', size=5)
    plt.rc('axes', labelsize=5)
    plt.rc('legend', fontsize=5)
    if param != "cpu":
        fig = plt.figure(figsize=(COLUMN_W, COLUMN_W - 1.2))
    else:
        fig = plt.figure(figsize=(COLUMN_W, COLUMN_W - 1.2))
    gs = fig.add_gridspec(2, 2)
    axes = gs.subplots(sharex=True, sharey=True)
    for n, ax in zip(SENS_TREES, axes.flatten()):
        results = []
        for csv_file in sorted(pathlib.Path(f"../results/sens/").glob(f"test_alg_sens_n{n}_{param}?.?.csv")):
            df = pd.read_csv(csv_file)
            df.dropna(subset=['Lat'], inplace=True)
            # df.loc[df.Cost == np.inf, "Time"] = 1000.0
            row = df[['Alg', 'Time']].groupby('Alg').median().transpose()
            param_value = csv_file.stem.rsplit(sep='_')[-1].lstrip(param)
            row.set_index(pd.Index([param_value], dtype=float, name=f"{param}"), inplace=True)
            results.append(row)
        df = pd.concat(results, ignore_index=False)
        for alg in PALGS:
            if alg not in df:
                continue
            ax.plot(df[alg], color=COLOR[alg], marker=MARKER[alg], markersize=M_SIZE, fillstyle=FILL[alg],
                    linewidth=LINE_W, linestyle=STYLES[alg], label=ALGS[alg])
        ax.grid(linestyle='dotted', zorder=0)
        ax.set_yscale('log')
        ax.set_xticks(df.index)
        # ax.set_xlabel('Tree size')
        ax.set_yticks(ax.get_yticks(), ax.get_yticklabels(), rotation=90, ha="center", va="center")
        ax.set_yscale('log')
        ax.set_ylim(bottom=2e-4, top=2e3)
        ax.yaxis.set_major_locator(mticker.LogLocator(numticks=7))
        ax.yaxis.set_minor_locator(mticker.LogLocator(subs="auto", numticks=8))
        ax.set_title(f"$n={n}$", pad=3)
    if param == "cpu":
        axes[0, 0].legend(loc="upper center", fancybox=True, framealpha=1, ncol=2, columnspacing=0.5)
    else:
        axes[0, 0].legend(loc="upper center", fancybox=True, framealpha=1, ncol=3, columnspacing=0.5)
    if param == "m":
        fig.supxlabel(r"Memory ratio $\rho_M$", ha="center", x=0.54)
    elif param == "l":
        fig.supxlabel(r"Latency ratio $\rho_{L_\pi}$", ha="center", x=0.54)
    elif param == "cpu":
        fig.supxlabel(r"vCPU count", ha="center", x=0.53)
    fig.supylabel("Median runtime [sec]", va="center", ha="center", y=0.54)
    plt.tight_layout(pad=0.6, h_pad=0.2, w_pad=0.2)
    if show:
        plt.show()
    else:
        plt.savefig(f"figs/alg_sens_ratio_{param}.{ext}")


def plot_bicrit_heatmap(n: int = 40, show: bool = True, ext: str = "pgf"):
    plt.style.use('fast')
    plt.rc('font', size=5)
    plt.rc('axes', labelsize=5)
    plt.rc('legend', fontsize=5)
    plt.figure(figsize=(COLUMN_W - 1.1, COLUMN_W - 1.9))
    results = collections.defaultdict(dict)
    for csv_file in sorted(pathlib.Path(f"../results/sens/").glob(f"test_alg_sens_n{n}_bicrit_*.csv")):
        df = pd.read_csv(csv_file)
        # df.loc[df.Cost == np.inf, "Time"] = 1000.0
        df.dropna(subset=['Lat'], inplace=True)
        t = df[['Alg', 'Time']].groupby('Alg').median()['Time'][0]
        eps, lam = map(float, csv_file.stem.rsplit(sep='_')[-1].split('-'))
        results[lam][eps] = t
    df = pd.DataFrame.from_dict(results, orient='index')
    df.columns.name = "eps"
    df.index.name = "lam"  # x: eps, y: lam
    df.sort_index(inplace=True)
    cax = plt.imshow(df, extent=(-0.05, 1.05, -0.05, 1.05), cmap='gray_r', interpolation='nearest', origin="lower",
                     norm='log', vmax=0.105, vmin=0.021)  # vmax=0.105, vmin=0.021
    cbar = plt.colorbar(cax, location="right", orientation="vertical", shrink=0.9, pad=0.1)
    cbar.set_label("Median runtime [sec]", labelpad=1, size=6)
    cbar.ax.yaxis.set_tick_params(which="major", labelsize=5, rotation=0)
    cbar.ax.yaxis.set_tick_params(which="minor", labelsize=4, rotation=0)
    xfmt = matplotlib.ticker.ScalarFormatter()
    xfmt.set_scientific(False)
    xfmt.set_useMathText(False)
    xfmt.set_powerlimits((-1, -1))
    cbar.ax.yaxis.set_major_formatter(xfmt)
    cbar.ax.yaxis.set_minor_formatter(xfmt)
    cbar.ax.yaxis.get_offset_text().set_position((7, 0))
    # cbar.ax.yaxis.set_ticklabels([1.00], minor=False)
    # cbar.ax.yaxis.set_ticklabels(cbar.ax.yaxis.get_ticklabels(minor=True), minor=True, va="top")
    plt.xlabel(r"Cost approximation ratio $\varepsilon$", size=6)
    plt.gca().set_xticks(np.linspace(0, 1, 6))
    plt.gca().xaxis.set_minor_locator(mticker.AutoMinorLocator(n=2))
    plt.xticks(ha="center", va="center")
    plt.ylabel(r"Latency violation ratio $\lambda$")
    plt.gca().set_yticks(np.linspace(0, 1, 6))
    plt.gca().yaxis.set_minor_locator(mticker.AutoMinorLocator(n=2))
    plt.yticks(rotation=90, va="center", ha="center")
    plt.tight_layout()
    if show:
        plt.show()
    else:
        plt.savefig(f"figs/alg_bicrit_heatmap.{ext}")


def plot_bicrit_runtimes(show: bool = True, ext: str = "pgf"):
    plt.style.use('fast')
    plt.rc('font', size=5)
    plt.rc('axes', labelsize=5)
    plt.rc('legend', fontsize=5)
    fig = plt.figure(figsize=(COLUMN_W, COLUMN_W - 0.7))
    gs = fig.add_gridspec(2, 1)
    axes = gs.subplots(sharex=True, sharey=True).flatten()
    params = ["lam", "eps"]
    for i, n in itertools.product((0, 1), SENS_TREES):
        results = []
        for csv_file in sorted(pathlib.Path(f"../results/sens/").glob(f"test_alg_sens_n{n}_{params[i]}?.?.csv")):
            df = pd.read_csv(csv_file)
            df.loc[df.Cost == np.inf, "Time"] = 1000.0
            row = df[['Alg', 'Time']].groupby('Alg').median().transpose()
            param_value = csv_file.stem.rsplit(sep='_')[-1].lstrip(params[i])
            row.set_index(pd.Index([param_value], dtype=float, name=f"{params[i]}"), inplace=True)
            results.append(row)
        df = pd.concat(results, ignore_index=False)
        axes[i].plot(df, color=PCOLOR['BIFPTAS_L'], marker=PMARKER['BIFPTAS_L'], markersize=M_SIZE,
                     fillstyle=PFILL['BIFPTAS_L'], linewidth=LINE_W, linestyle=PSTYLES['BIFPTAS_L'], label=n)
        axes[i].grid(linestyle='dotted', zorder=0)
        axes[i].set_xlabel(f"{params[i]}")
        axes[i].set_xticks(df.index)
    # plt.xlabel("Tree Size ($n$)")  # ,labelpad=1)
    plt.yticks(rotation=90, ha="center", va="center")
    plt.yscale('log')
    plt.ylim(bottom=1e-2, top=1e1)
    plt.ylabel("Median runtime [sec]")  # ,labelpad=1)
    axes[0].legend(loc="upper right", fancybox=True, framealpha=1, ncol=4, columnspacing=0.5,
                   title=r"$n$")  # labelspacing=0.5)
    plt.tight_layout()
    if show:
        plt.show()
    else:
        plt.savefig(f"figs/alg_bicrit_runtimes.{ext}")


########################################################################################################################

# CALGS = dict(BASELINE_NO_PART="NoPart", BASELINE_SINGLE="Singleton", MINW_CHAIN="MinWCut",
#              K_SPLIT="Ksplit", CHAIN_PART="ChainTP", COSTLESS="COSTLESS",
#              BIFPTAS="BiFPTAS", MINW_HEUR="GrTP", PSEUDO_L_PAR="LRTP", OPT="MtxILP")

CALGS = dict(BASELINE_NO_PART="NoFusion", BASELINE_SINGLE="Singleton", MINW_CHAIN="MinWCut",
             K_SPLIT_EXH="MinKSplit", CHAIN_PART_SER="ChainTP", COSTLESS="Costless",
             BIFPTAS="BiFPTAS", MINW_HEUR="GrTP", OPT="MtxILP")

CSTYLES = dict(BASELINE_NO_PART=":", BASELINE_SINGLE="-", MINW_CHAIN="--",
               K_SPLIT_EXH="--", CHAIN_PART_SER="--", COSTLESS="--",
               OPT="-", PSEUDO_L_PAR=":", BIFPTAS="--", MINW_HEUR="-.",
               GREEDY_PAR="-.", OPT_PAR="-")

CCOLOR = dict(BASELINE_NO_PART="m", BASELINE_SINGLE="m", MINW_CHAIN="c",
              K_SPLIT_EXH="y", CHAIN_PART_SER="y", COSTLESS="y",
              OPT="g", PSEUDO_L_PAR="k", BIFPTAS="b", MINW_HEUR="r",
              GREEDY_PAR="r", OPT_PAR="g")

CMARKER = dict(BASELINE_NO_PART="P", BASELINE_SINGLE="v", MINW_CHAIN="o",
               K_SPLIT_EXH="x", CHAIN_PART_SER="^", COSTLESS="s",
               OPT="o", PSEUDO_L_PAR="s", BIFPTAS="s", MINW_HEUR="D",
               GREEDY_PAR="D", OPT_PAR="o")

CFILL = dict(BASELINE_NO_PART="full", BASELINE_SINGLE="none", MINW_CHAIN="none",
             K_SPLIT_EXH="full", CHAIN_PART_SER="full", COSTLESS="none",
             OPT="full", PSEUDO_L_PAR="full", BIFPTAS="none", MINW_HEUR="none",
             GREEDY_PAR="none", OPT_PAR="full")


def plot_cost_runtimes(tree_type: str = "random", show: bool = True, ext: str = "pgf"):
    plt.style.use('fast')
    plt.rc('font', size=5)
    plt.rc('axes', labelsize=6)
    plt.rc('legend', fontsize=5)
    # plt.figure(figsize=(TEXT_W / 3, COLUMN_W - 1.7))
    plt.figure(figsize=(COLUMN_W, COLUMN_W - 2))
    results = []
    for csv_file in sorted(pathlib.Path(f"../results/cost/").glob(f"test_alg_cost_{tree_type}_tree_n*.csv")):
        df = pd.read_csv(csv_file)
        # df.loc[df.Cost == np.inf, "Time"] = 1000.0
        df.dropna(subset=['Lat'], inplace=True)
        row = df[['Alg', 'Time']].groupby('Alg').median().transpose()
        n1, n2 = map(int, csv_file.stem.rsplit(sep='n')[-1].split('-'))
        row.set_index(pd.IntervalIndex.from_tuples([(n1, n2)], dtype="interval[int64, left]'", closed="left",
                                                   name=f"Tree Size"), inplace=True)
        results.append(row)
    df = pd.concat(results, ignore_index=False)
    for alg in CALGS:
        plt.plot(list(map(str, df[alg].index.values)), list(df[alg]), color=CCOLOR[alg], marker=CMARKER[alg],
                 markersize=M_SIZE, fillstyle=CFILL[alg], linewidth=LINE_W, linestyle=CSTYLES[alg], label=CALGS[alg])
    plt.grid(linestyle='dotted', zorder=0)
    plt.margins(x=0.03)
    plt.gca().set_xticklabels([tl._text.replace(' ', '') for tl in plt.gca().get_xticklabels()])
    plt.xlabel("Tree size intervals ($n$)")
    plt.ylim(bottom=2e-4, top=2e3)
    plt.yticks(rotation=90, ha="center", va="center")
    plt.yscale('log')
    plt.ylabel("Median runtime [sec]")  # , labelpad=2)  # ,labelpad=1)
    plt.gca().yaxis.set_major_locator(mticker.LogLocator(numticks=8))
    # plt.gca().yaxis.set_minor_locator(mticker.AutoMinorLocator(n=2))
    if tree_type == "job":
        # plt.legend(loc="upper center", fancybox=True, framealpha=1, ncol=3, columnspacing=0.5)
        plt.legend(loc="upper left", fancybox=True, framealpha=1, ncol=3, columnspacing=0.5)
    plt.tight_layout(pad=0.3)
    if show:
        plt.show()
    else:
        plt.savefig(f"figs/alg_cost_runtimes_{tree_type}.{ext}")


def check_part_feasibility(row: list, npy_file: str) -> bool:
    if pd.isna(row['Lat']):
        return False
    else:
        tree = get_tree_from_file(npy_file, int(row['Tree'].split('_')[-1]))
        barrs = list(map(int, row['Part'][1:-1].split('|')))
        M = int(row['M'])
        for _, nodes in isubtrees(tree, barrs):
            if ser_subtree_memory(tree, nodes) > M:
                return False
        return True


def check_part_solvable(row: list) -> bool:
    return False if pd.isna(row['Lat']) else True


def plot_cost_ser_valid(tree_type: str = "faas", n=40, show: bool = True, feasible: bool = True, ext: str = "pgf"):
    plt.style.use('fast')
    plt.rc('font', size=5)
    plt.rc('axes', labelsize=5)
    plt.rc('legend', fontsize=5)
    df = pd.read_csv(f"../results/cost/test_alg_cost_{tree_type}_tree_n{n}-{n + 10}.csv")
    df.loc[df.Cost == np.inf, "Time"] = 1000.0
    df2 = df[['Tree', 'Alg', 'Cost']]
    df2 = df2.set_index(['Tree', 'Alg'])
    for t in df.Tree.unique():
        df2.loc[[t]] = (df2.loc[[t]] - df2.loc[t, "OPT"].Cost) / df2.loc[t, "OPT"].Cost
    df2.reset_index(inplace=True)
    df2['Lat'] = (df['Lat'] - df['L']) / df['L']
    if feasible:
        df2['Feasible'] = df.apply(check_part_feasibility, axis=1,
                                   args=(f"../data/{tree_type}_tree_n{n}-{n + 10}.npy",))
        df2['Solvable'] = df.apply(check_part_solvable, axis=1)
    # df2.dropna(subset=['Lat'], inplace=True)
    fig = plt.figure(figsize=(COLUMN_W, COLUMN_W - 0.5))
    gs = fig.add_gridspec(3, 3)
    axes = gs.subplots(sharex=True, sharey=True)
    for alg, ax in zip(CALGS.keys(), axes.flatten()):
        ax.axhline(0, color='k', linewidth=0.5)
        ax.axvline(0, color='k', linewidth=0.5)
        # df2[df2.Alg == alg][['Cost', 'Lat']].plot.scatter(x="Cost", y="Lat", ax=ax)
        data = df2[df2.Alg == alg][['Cost', 'Lat', 'Feasible', 'Solvable']]
        # ax.scatter(x=data["Cost"], y=data["Lat"], s=2, c='g', marker=".", zorder=2)
        # color = data.apply(lambda r: 'green' if r['Feasible'] else 'gray', axis=1)
        # ax.scatter(x=data["Cost"], y=data["Lat"], s=2, c=color, marker=".", zorder=2)
        data_infeasible = data[~data['Feasible']]
        ax.scatter(x=data_infeasible["Cost"], y=data_infeasible["Lat"], s=2, c='red', marker=".",
                   label="Overbooked" if alg == "BASELINE_SINGLE" else None, zorder=2)
        print(f"{alg} - Infeasible:", data_infeasible['Cost'].count())
        data_feasible = data[data['Feasible']]
        ax.scatter(x=data_feasible["Cost"], y=data_feasible["Lat"], s=2, c='green', marker=".",
                   label="$M$-feasible" if alg == "BASELINE_NO_PART" else None, zorder=2)
        print(f"{alg} - Feasible:", data_feasible['Cost'].count())
        print(f"{alg} - Unsolvable:", data[~data['Solvable']]['Cost'].count())
        print('-' * 10)
        ax.grid(linestyle='dotted', zorder=-2)
        ax.set_title(CALGS[alg], pad=3)
        if alg == "BIFPTAS":
            # arc = matplotlib.patches.Arc((0, 0), 0.5, 0.5, theta1=0, theta2=180, color='r')
            # ax.add_patch(arc)
            ax.autoscale(False)
            ax.axvline(0.5, color="b", linestyle="--", linewidth=0.5, label=r"$\varepsilon= 0.5$")
            ax.axhline(0.5, color="r", linestyle="--", linewidth=0.5, label=r"$\lambda = 0.5$")
            # ax.axvline(0.5, color="b", linestyle="--", linewidth=0.5, label=r"$\varepsilon = 0.5$")
            ax.legend(loc="upper center", fancybox=True, framealpha=1, ncol=2, handlelength=1, columnspacing=0.75,
                      handletextpad=0.2, borderpad=0.4)
    fig.supxlabel("Cost deviation from optimum", ha="center", x=0.53)
    fig.supylabel(r"Latency deviation from $L_\pi$", va="center", y=0.535)
    plt.gca().xaxis.set_minor_locator(mticker.AutoMinorLocator(n=2))
    plt.gca().yaxis.set_major_locator(mticker.MultipleLocator())
    plt.gca().yaxis.set_minor_locator(mticker.AutoMinorLocator(n=2))
    axes[0, 0].legend(loc="upper center", fancybox=True, framealpha=1, ncol=1,
                      handlelength=1, columnspacing=0.75, handletextpad=0.2, borderpad=0.3)
    axes[0, 1].legend(loc="upper center", fancybox=True, framealpha=1, ncol=1,
                      handlelength=1, columnspacing=0.75, handletextpad=0.2, borderpad=0.3)
    axes[0, 0].set_xlim(left=-0.11, right=0.82)
    axes[0, 0].set_ylim(bottom=-1.2, top=4.2)
    for ax_line in axes:
        ax_line[0].set_yticklabels(ax_line[0].get_yticklabels(), rotation=90, ha="center", va="center")
    for ax in axes.flatten():
        ax.autoscale(False)
        y_min, y_max = ax.get_ylim()
        x_min, x_max = ax.get_xlim()
        x_split_ratio = abs(x_min) / (x_max - x_min)
        ax.axhspan(y_min, 0, 0, x_split_ratio, facecolor="grey", alpha=0.5)
        ax.axhspan(0, y_max, x_split_ratio, 1, facecolor="red", alpha=0.1)
    plt.tight_layout(pad=0.8, w_pad=0.3)
    if show:
        plt.show()
    else:
        plt.savefig(f"figs/alg_cost_ser_valid_{tree_type}.{ext}")


PCALGS = dict(CHAIN_PART_PAR="parChainTP", COSTLESS_PAR="parCOSTLESS",
              GREEDY_PAR="parGrTP")  # OPT_PAR="parMtxILP", PSEUDO_L_PAR="parLRTP")


def plot_cost_par_valid(tree_type: str = "faas", n=40, show: bool = True, feasible: bool = True, ext: str = "pgf"):
    plt.style.use('fast')
    plt.rc('font', size=5)
    plt.rc('axes', labelsize=5)
    plt.rc('legend', fontsize=5)
    df = pd.read_csv(f"../results/cost/test_alg_cost_{tree_type}_tree_n{n}-{n + 10}.csv")
    df.loc[df.Cost == np.inf, "Time"] = 1000.0
    df2 = df[['Tree', 'Alg', 'Cost']]
    df2 = df2.set_index(['Tree', 'Alg'])
    for t in df.Tree.unique():
        df2.loc[[t]] = (df2.loc[[t]] - df2.loc[t, "OPT_PAR"].Cost) / df2.loc[t, "OPT"].Cost
    df2.reset_index(inplace=True)
    df2['Lat'] = (df['Lat'] - df['L']) / df['L']
    if feasible:
        df2['Feasible'] = df.apply(check_part_feasibility, axis=1,
                                   args=(f"../data/{tree_type}_tree_n{n}-{n + 10}.npy",))
        df2['Solvable'] = df.apply(check_part_solvable, axis=1)
    fig = plt.figure(figsize=(COLUMN_W, (COLUMN_W - 0.5) / 3))
    gs = fig.add_gridspec(1, 3)
    axes = gs.subplots(sharex=True, sharey=True).flatten()
    for alg, ax in zip(PCALGS, axes):
        ax.axhline(0, color='k', linewidth=0.5)
        ax.axvline(0, color='k', linewidth=0.5)
        data = df2[df2.Alg == alg][['Cost', 'Lat', 'Feasible', 'Solvable']]
        data_infeasible = data[~data['Feasible']]
        ax.scatter(x=data_infeasible["Cost"], y=data_infeasible["Lat"], s=2, c='red', marker=".",
                   label="Overbooked" if alg == "BASELINE_NO_PART" else None, zorder=2)
        print(f"{alg} - Infeasible:", data_infeasible['Cost'].count())
        data_feasible = data[data['Feasible']]
        ax.scatter(x=data_feasible["Cost"], y=data_feasible["Lat"], s=2, c='green', marker=".",
                   label="$M$-feasible" if alg == "PSEUDO_L_PAR" else None, zorder=2)
        print(f"{alg} - Feasible:", data_feasible['Cost'].count())
        print(f"{alg} - Unsolvable:", data[~data['Solvable']]['Cost'].count())
        print('-' * 10)
        ax.grid(linestyle='dotted', zorder=-2)
        ax.set_title(PCALGS[alg], pad=3)
    fig.supxlabel("Cost deviation from optimum (parMtxILP)", ha="center", x=0.57)
    fig.supylabel("Latency dev.\nfrom $L_\pi$", multialignment='center', va="center", y=0.6)
    # plt.gca().xaxis.set_minor_locator(mticker.AutoMinorLocator(n=2))
    # axes[0].legend(loc="upper center", fancybox=True, framealpha=1, ncol=1, labelspacing=0.2, handletextpad=0.1)
    # for ax in axes:
    #     ax.set_yticklabels(ax.get_yticklabels(), rotation=90)
    # axes[0].set_ylim(-0.4, 0.1)

    axes[0].yaxis.set_major_locator(mticker.MultipleLocator(0.5))
    axes[0].yaxis.set_minor_locator(mticker.AutoMinorLocator(n=2))
    axes[0].xaxis.set_minor_locator(mticker.AutoMinorLocator(n=2))
    axes[0].set_yticks(axes[0].get_yticks(), axes[0].get_yticklabels(), rotation=90, va='center')
    plt.xlim(-0.1, 1.1)
    plt.ylim(-1.1, 0.25)
    # plt.yticks(rotation=90)
    for ax in axes:
        ax.autoscale(False)
        y_min, y_max = ax.get_ylim()
        x_min, x_max = ax.get_xlim()
        x_split_ratio = abs(x_min) / (x_max - x_min)
        ax.axhspan(y_min, 0, 0, x_split_ratio, facecolor="grey", alpha=0.5)
        ax.axhspan(0, y_max, x_split_ratio, 1, facecolor="red", alpha=0.2)
    plt.tight_layout(pad=0.8, w_pad=0.3)
    if show:
        plt.show()
    else:
        plt.savefig(f"figs/alg_cost_par_valid_{tree_type}.{ext}")


_RED = (1.000000, 0.752941, 0.796078)
_GREEN = (0.564706, 0.933333, 0.564706)
_BLUE = (0.678431, 0.847059, 0.901961)

_LRED = (1.000000, 0.874509, 0.894117)
_LGREEN = (0.780392, 0.964705, 0.780392)
_LBLUE = (0.835294, 0.921568, 0.949019)


def plot_cost_valid_bar(n=40, show: bool = True, ext: str = "pgf"):
    plt.style.use('fast')
    plt.rc('font', size=5)
    plt.rc('axes', labelsize=5)
    plt.rc('legend', fontsize=5)
    plt.rc('axes', linewidth=0.5)

    fig, ax = plt.subplots(figsize=(COLUMN_W + 0.5, COLUMN_W / 3 + 0.2))
    idx = np.array(range(1, len(CALGS) + 1))

    for _type, off in zip(("job", "faas"), (-0.2, 0.2)):
        df = pd.read_csv(f"../results/cost/test_alg_cost_{_type}_tree_n{n}-{n + 10}.csv")
        df.loc[df.Cost == np.inf, "Time"] = 1000.0
        df2 = df[['Tree', 'Alg', 'Cost']]
        df2 = df2.set_index(['Tree', 'Alg'])
        for t in df.Tree.unique():
            df2.loc[[t]] = (df2.loc[[t]] - df2.loc[t, "OPT"].Cost) / df2.loc[t, "OPT"].Cost
        df2.reset_index(inplace=True)
        df2['Lat'] = (df['Lat'] - df['L']) / df['L']
        df2['Feasible'] = df.apply(check_part_feasibility, axis=1, args=(f"../data/{_type}_tree_n{n}-{n + 10}.npy",))
        df2['Solvable'] = df.apply(check_part_solvable, axis=1)
        cnt = {"F": [], "I": [], "U": []}
        for alg in CALGS.keys():
            data = df2[df2.Alg == alg][['Cost', 'Lat', 'Feasible', 'Solvable']]
            c_feasible = data[data['Feasible'] & data['Lat'].le(0)]['Cost'].count()
            c_infeasible = data[~data['Feasible'] & data['Solvable'] | data['Lat'].gt(0)]['Cost'].count()
            c_unsolvable = data[~data['Solvable']]['Cost'].count()
            print(alg, c_feasible, c_infeasible, c_unsolvable)
            cnt["F"].append(c_feasible)
            cnt["I"].append(c_infeasible)
            cnt["U"].append(c_unsolvable)

        # plt.grid(linestyle='dotted', zorder=2)
        cnt_label = {"F": r"Feasible", "I": r"Infeasible wrt. $M$ and/or $L_\pi$", "U": r"Unsolvable"}
        bottom = np.zeros(len(CALGS))
        for k, cb, ce, h in zip(cnt.keys(), (_LGREEN, _LRED, _LBLUE), (_GREEN, _RED, _BLUE), ("", "", "")):
            v = np.array(cnt[k])
            v_plot = np.where(v == 0, np.nan, v)
            ax.bar(idx + off, v_plot, bottom=bottom, width=0.4, label=cnt_label[k] if _type == "job" else None,
                   color=cb, edgecolor=ce, lw=0.5, hatch=h, zorder=2)
            bottom += v

        for c in ax.containers:
            labels = [int(v.get_height()) if v.get_height() > 0 else '' for v in c]
            ax.bar_label(c, label_type='center', labels=labels)  # add a container object "c" as first argument

    plt.ylim(top=124)
    plt.xlim(0.4, 9.6)
    plt.yticks(rotation=90, ha="center", va="center")
    plt.ylabel("Number of test cases")
    plt.xticks(idx, CALGS.values())
    plt.xlabel("Tree Partitioning Methods")
    plt.grid(linestyle='dotted', zorder=0)
    plt.legend(loc="upper center", fancybox=True, framealpha=1, ncol=3)
    plt.tight_layout(pad=0.8, w_pad=0.1)

    if show:
        plt.show()
    else:
        plt.savefig(f"figs/alg_cost_valid_bar.{ext}")


if __name__ == '__main__':
    # plot_alg_runtimes(alg_type="serial", show=True)
    # plot_alg_runtimes(alg_type="parallel", show=True)
    # plot_sens_runtimes(param="m", show=True)
    # plot_sens_runtimes(param="l", show=True)
    # plot_sens_runtimes(param="cpu", show=True)
    # plot_bicrit_heatmap(n=40, show=True)
    # plot_bicrit_runtimes(show=True)
    # plot_cost_runtimes(tree_type="random", show=True)
    # plot_cost_runtimes(tree_type="job", show=True)
    # plot_cost_runtimes(tree_type="faas", show=True)
    # plot_cost_ser_valid(tree_type="random", n=40, show=True)
    # plot_cost_ser_valid(tree_type="job", n=40, show=True)
    # plot_cost_ser_valid(tree_type="faas", n=40, show=True)
    # plot_cost_par_valid(tree_type="random", n=40, show=True)
    # plot_cost_par_valid(tree_type="job", n=40, show=True)
    # plot_cost_par_valid(tree_type="faas", n=40, show=True)
    #
    # plot_alg_runtimes(alg_type="serial", show=False, ext="pgf")
    # plot_alg_runtimes(alg_type="serial", show=False, ext="pdf")
    # plot_alg_runtimes(alg_type="parallel", show=False, ext="pgf")
    # plot_alg_runtimes(alg_type="parallel", show=False, ext="pdf")
    #
    # plot_sens_runtimes(param="m", show=False, ext="pgf")
    # plot_sens_runtimes(param="m", show=False, ext="pdf")
    # plot_sens_runtimes(param="l", show=False, ext="pgf")
    # plot_sens_runtimes(param="l", show=False, ext="pdf")
    # plot_sens_runtimes(param="cpu", show=False, ext="pgf")
    # plot_sens_runtimes(param="cpu", show=False, ext="pdf")
    #
    # plot_bicrit_heatmap(show=False, ext="pgf")
    # plot_bicrit_heatmap(show=False, ext="pdf")
    #
    # plot_cost_runtimes(tree_type="random", show=False, ext="pgf")
    # plot_cost_runtimes(tree_type="random", show=False, ext="pdf")
    # plot_cost_runtimes(tree_type="job", show=False, ext="pgf")
    # plot_cost_runtimes(tree_type="job", show=False, ext="pdf")
    # plot_cost_runtimes(tree_type="faas", show=False, ext="pgf")
    # plot_cost_runtimes(tree_type="faas", show=False, ext="pdf")
    #
    # plot_cost_ser_valid(tree_type="random", show=False, ext="pgf")
    # plot_cost_ser_valid(tree_type="random", show=False, ext="pdf")
    # plot_cost_ser_valid(tree_type="faas", show=False, ext="pgf")
    # plot_cost_ser_valid(tree_type="faas", show=False, ext="pdf")
    # plot_cost_ser_valid(tree_type="job", show=False, ext="pgf")
    # plot_cost_ser_valid(tree_type="job", show=False, ext="pdf")
    #
    # plot_cost_par_valid(tree_type="random", n=40, show=False, ext="pgf")
    # plot_cost_par_valid(tree_type="random", n=40, show=False, ext="pdf")
    # plot_cost_par_valid(tree_type="job", n=40, show=False, ext="pgf")
    # plot_cost_par_valid(tree_type="job", n=40, show=False, ext="pdf")
    # plot_cost_par_valid(tree_type="faas", n=40, show=False, ext="pgf")
    # plot_cost_par_valid(tree_type="faas", n=40, show=False, ext="pdf")
    #
    # plot_cost_valid_bar(tree_type="job", n=40, show=True, ext="pdf")
    # plot_cost_valid_bar(n=40, show=True, ext="pgf")
    plot_cost_valid_bar(n=40, show=False, ext="pgf")
