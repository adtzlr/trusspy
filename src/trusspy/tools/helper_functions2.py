# -*- coding: utf-8 -*-
"""
title: TrussPy - Truss Solver for Python
author: Andreas Dutzler
year: 2023
"""

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d


class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0, 0), (0, 0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def do_3d_projection(self, renderer=None):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, self.axes.M)
        self.set_positions((xs[0], ys[0]), (xs[1], ys[1]))
        return np.min(zs)


def plot_coord(ax, a=1.0):
    ax.plot([0, a], [0, 0], [0, 0], alpha=0)
    ax.plot([0, 0], [0, a], [0, 0], alpha=0)
    ax.plot([0, 0], [0, 0], [0, a], alpha=0)
    ax.plot([0], [0], [0], "ko", ms=10)
    arrow_properties = dict(
        mutation_scale=20, lw=3, arrowstyle="-|>", color="k", shrinkA=0, shrinkB=0
    )
    x1 = Arrow3D([0, a], [0, 0], [0, 0], **arrow_properties)
    x2 = Arrow3D([0, 0], [0, a], [0, 0], **arrow_properties)
    x3 = Arrow3D([0, 0], [0, 0], [0, a], **arrow_properties)
    ax.add_artist(x1)
    ax.add_artist(x2)
    ax.add_artist(x3)
    return ax


def plot_hist(x, y, nl, xl, yl="LPF", fig=None, ax=None):
    if fig is None:
        fig, ax = plt.subplots()
    ax.plot(x, y, ".-", label="Node " + str(int(nl)))
    ax.set_xlabel(xl)
    ax.set_ylabel(yl)
    ax.legend()
    plt.gcf().set_size_inches(8, 6)
    return fig, ax


def plot_pth(x, y, inc, yl="LPF", fig=None, ax=None):
    if fig is None:
        fig, ax = plt.subplots()
    if x == range(min(x), max(x) + 1):
        xx = np.linspace(min(x), max(x), 11, dtype=int)
        xdata = x
        xtcks = xx
        xtckl = xx
    else:
        xx = np.array(x, dtype=int)[::]
        xdata = range(len(xx))
        xtcks = range(len(xx))
        xtckl = xx

    ax.plot(xdata, y, ".-", label="Increment " + str(int(inc)))
    ax.set_xlabel("Nodepath")
    ax.set_ylabel(yl)
    ax.set_xticks(xtcks)
    ax.set_xticklabels(xtckl)
    ax.legend()
    plt.gcf().set_size_inches(8, 6)
    return fig, ax


def plot_nodes(X, fig=None, ax=None, view="xz", color="k", size=10):
    if view == "xz":
        i, j = 0, 2
    if view == "xy":
        i, j = 0, 1
    if view == "yz":
        i, j = 1, 2

    if view == "3d":

        if fig is None:
            fig = plt.figure()
        if ax is None:
            ax = fig.add_subplot(111, projection="3d")

        ax.plot(X[:, 0], X[:, 1], X[:, 2], color + "o", ms=size, zorder=30)
    else:
        plt.scatter(X[:, i], X[:, j], marker="o", s=15 * size, color=color, zorder=30)
        fig = plt.gcf()
        ax = plt.gca()

    return fig, ax


def plot_force(f0, X, fig=None, ax=None, view="xz", color="C2", scale=0.5):
    if view == "xz":
        i, j, k = 0, 2, 1
    if view == "xy":
        i, j, k = 0, 1, 2
    if view == "yz":
        i, j, k = 1, 2, 0
    if view == "3d":
        i, j, k = 0, 1, 2
    for f0i, Xi in zip(f0, X):
        if ~(f0i == np.zeros(3)).all():
            xx = Xi[i]
            yy = Xi[j]
            if view == "3d":
                zz = Xi[k]
            if f0i[i] < 0:
                pass
            if f0i[j] < 0:
                pass

            if view == "3d":

                if fig is None:
                    fig = plt.figure()
                if ax is None:
                    ax = fig.add_subplot(111, projection="3d")

                arrow_properties = dict(
                    mutation_scale=20,
                    lw=3,
                    arrowstyle="-|>",
                    color=color,
                    shrinkA=0,
                    shrinkB=0,
                    zorder=20,
                )
                if f0i[k] != 0:
                    ax.plot(
                        [xx, xx],
                        [yy, yy],
                        [zz, zz + scale * f0i[k]],
                        alpha=0,
                    )
                    a = Arrow3D(
                        [xx, xx],
                        [yy, yy],
                        [zz, zz + scale * f0i[k]],
                        **arrow_properties
                    )
                    ax.add_artist(a)

                if f0i[j] != 0:
                    ax.plot(
                        [xx, xx],
                        [yy, yy + scale * f0i[j]],
                        [zz, zz],
                        alpha=0,
                    )
                    a = Arrow3D(
                        [xx, xx],
                        [yy, yy + scale * f0i[j]],
                        [zz, zz],
                        **arrow_properties
                    )
                    ax.add_artist(a)

                if f0i[i] != 0:
                    ax.plot(
                        [xx, xx + scale * f0i[i]],
                        [yy, yy],
                        [zz, zz],
                        alpha=0,
                    )
                    a = Arrow3D(
                        [xx, xx + scale * f0i[i]],
                        [yy, yy],
                        [zz, zz],
                        **arrow_properties
                    )
                    ax.add_artist(a)
            else:  # 2d
                fig = plt.gcf()
                ax = plt.gca()
                if f0i[i] != 0:
                    plt.arrow(
                        xx,
                        yy,
                        scale * f0i[i],
                        0,
                        color=color,
                        linewidth=3,
                        zorder=20,
                        width=0.025,
                        length_includes_head=True,
                    )
                    plt.plot([xx, xx + scale * f0i[i]], [yy, yy + 0], alpha=0)
                if f0i[j] != 0:
                    plt.arrow(
                        xx,
                        yy,
                        0,
                        scale * f0i[j],
                        color=color,
                        linewidth=3,
                        zorder=20,
                        width=0.025,
                        length_includes_head=True,
                    )
                    plt.plot([xx, xx + 0], [yy, yy + scale * f0i[j]], alpha=0)

    return fig, ax


def plot_elems(
    E, X, fig=None, ax=None, view="xz", color="C0", contour=None, lim_scale=1.2
):

    if view == "xz":
        i, j = 0, 2
    if view == "xy":
        i, j = 0, 1
    if view == "yz":
        i, j = 1, 2

    if contour is not None:
        clabel = contour[0]
        contour_lim = contour[2]
        contour = contour[1]

    for k, e in enumerate(E):
        NA = int(e[-2])
        NE = int(e[-1])

        if contour is not None:
            # build up colormap and normalizer
            colormap = plt.get_cmap("bwr", 10)
            colormap.set_over("0.95")
            colormap.set_under("0.6")

            if contour_lim is None:
                norm = mpl.colors.Normalize(vmin=min(contour), vmax=max(contour))
            else:
                norm = mpl.colors.Normalize(vmin=contour_lim[0], vmax=contour_lim[1])
            color = colormap(norm(contour[k]))

            # create a ScalarMappable and initialize a data structure
            s_m = mpl.cm.ScalarMappable(cmap=colormap, norm=norm)
            s_m.set_array([])

        if view == "3d":

            if fig is None:
                fig = plt.figure()
            if ax is None:
                ax = fig.add_subplot(111, projection="3d")
            if contour is not None:
                ax.plot(
                    [X[NA - 1][0], X[NE - 1][0]],
                    [X[NA - 1][1], X[NE - 1][1]],
                    [X[NA - 1][2], X[NE - 1][2]],
                    color="C7",
                    zorder=1,
                    linewidth=8.0,
                )
            ax.plot(
                [X[NA - 1][0], X[NE - 1][0]],
                [X[NA - 1][1], X[NE - 1][1]],
                [X[NA - 1][2], X[NE - 1][2]],
                color=color,
                zorder=2,
                linewidth=6.0,
            )
        else:  # 2d
            if contour is not None:
                (line,) = plt.plot(
                    [X[NA - 1][i], X[NE - 1][i]],
                    [X[NA - 1][j], X[NE - 1][j]],
                    color="C7",
                    zorder=1,
                    linewidth=8.0,
                )
            (line,) = plt.plot(
                [X[NA - 1][i], X[NE - 1][i]],
                [X[NA - 1][j], X[NE - 1][j]],
                color=color,
                zorder=2,
                linewidth=6.0,
            )

    if contour is not None:
        plt.colorbar(
            s_m,
            extend="both",
            ticks=np.linspace(contour_lim[0], contour_lim[1], 11),
            ax=plt.gca(),
        )
        plt.ylabel("CONTOUR = " + clabel)

    try:
        if len(lim_scale) == 2:
            minx, maxx = lim_scale
            miny, maxy = minx, maxx
            plt.xlim(minx, maxx)
            plt.ylim(miny, maxy)
        elif len(lim_scale) == 4:
            minx, maxx, miny, maxy = lim_scale
            plt.xlim(minx, maxx)
            plt.ylim(miny, maxy)
        elif len(lim_scale) == 6:
            minx, maxx, miny, maxy, minz, maxz = lim_scale
            ax.set_xlim(minx, maxx)
            ax.set_ylim(miny, maxy)
            ax.set_zlim(minz, maxz)
            m = 0.5 * min(maxx, maxy, maxz)
            xx, yy = np.meshgrid(np.linspace(0, m, 2), np.linspace(0, m, 2))
            ax = plot_coord(ax, m)
            zz = np.zeros_like(xx)
            ax.plot_surface(xx, yy, zz, alpha=0.2)
            ax.view_init(20, -40)

    except:
        m = lim_scale * max(
            abs(plt.xlim()[0]),
            abs(plt.xlim()[1]),
            abs(plt.ylim()[0]),
            abs(plt.ylim()[1]),
        )

        if lim_scale < 0:
            m = -lim_scale
        else:
            alimx = (plt.xlim()[1] - plt.xlim()[0]) / 2
            alimy = (plt.ylim()[1] - plt.ylim()[0]) / 2
            mlimx = (plt.xlim()[1] + plt.xlim()[0]) / 2
            mlimy = (plt.ylim()[1] + plt.ylim()[0]) / 2
            alim = lim_scale * max(alimx, alimy)
            minx, maxx = (mlimx - alim, mlimx + alim)
            miny, maxy = (mlimy - alim, mlimy + alim)
            if abs(lim_scale) < 100:
                plt.xlim(minx, maxx)
                plt.ylim(miny, maxy)

        if view == "3d":
            if abs(lim_scale) < 100:
                ax.set_xlim(-m, m)
                ax.set_ylim(-m, m)
                ax.set_zlim(-m, m)
                xx, yy = np.meshgrid(np.linspace(0, m, 2), np.linspace(0, m, 2))
                ax = plot_coord(ax, m)
            else:
                xx, yy = np.meshgrid(np.linspace(0, 1, 2), np.linspace(0, 1, 2))
                ax = plot_coord(ax, 1)
            zz = np.zeros_like(xx)
            ax.plot_surface(xx, yy, zz, alpha=0.2)
            ax.view_init(20, -40)
        else:
            plt.gca().set_aspect("equal")
            if lim_scale < 0 and abs(lim_scale) < 100:
                plt.xlim(-m, m)
                plt.ylim(-m, m)

    plt.gcf().set_size_inches(8, 6)

    return fig, ax
