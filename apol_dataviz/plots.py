# Functions for making a variety of specific types of plot.
# Please note: these functions only work properly if the house style has been set.
# Therefore be aware that importing these functions has that side-effect, i.e. the
# Apolitical house style will be set upon import.

from apol_dataviz.style import use_apol_style

use_apol_style()

from apol_dataviz.colors import ColorDefinitions

color_definitions = ColorDefinitions()

import numpy as np
import matplotlib.pyplot as plt

plt.ion()
import seaborn as sns


def doughnut(data, kind="categorical", sortvals=True, hole_radius=0.6):

    """
    doughnut

    Makes a doughnut plot (better than a bar chart). Various different
    flavours are available.

    INPUTS:
        data - pandas Series

    KEYWORDS:
        kind = "categorical" - style; one of {"categorical", "sequential", "plain"}
        sortvals = True      - sort the values before plotting
        hole_radius = 0.6    - change the look of the doughnut chart

    OUTPUTS:
        axis - matplotlib axis object

    """

    if kind == "categorical":
        plotargs = {"labeldistance": 1.2}

    elif kind == "sequential":
        # build a sequential palette, but soften the color differences by one unit
        plotargs = {
            "labeldistance": 1.2,
            "colors": color_definitions.apol_navy_pal(data.size + 1, reverse=True)[:-1],
        }

    else:
        plotargs = {
            "labeldistance": 1.2,
            "colors": [color_definitions.blueTeal],
            "wedgeprops": {"linewidth": 3, "edgecolor": "white"},
        }

    # if sortvals == True, sort the data before plotting
    plot_data = data.sort_values(ascending=False) if sortvals else data

    # create a piechart
    axis = plot_data.plot.pie(**plotargs)

    # add the central hole to turn it into a doughnut
    axis.add_artist(plt.Circle((0, 0), hole_radius, color="white"))

    return axis


def hbarplot(data, categorical=False):

    """
    hbarplot

    This function creates a horizontal bar plot. If the bars represent
    categories, the default palette is used. If they do not, then you can
    instead plot all bars the same color, with a nice gradient fill.

    INPUTS:
        data - pandas Series for plotting

    KEYWORDS:
        categorical = False - if True, plot bars using to default palette

    OUTPUTS:
        axis - matplotlib axis object

    """

    # note the reversal of the data; fixes unintuitive ordering of plot.barh
    axis = data.iloc[::-1].plot.barh()

    if categorical:
        axis.grid(axis="y")
        return axis

    bars = axis.patches

    grad = np.atleast_2d(np.linspace(0, 1, 256))

    xlim = axis.get_xlim()
    ylim = axis.get_ylim()

    for bar in bars:
        bar.set_facecolor("none")
        x, y = bar.get_xy()
        w, h = bar.get_width(), bar.get_height()
        axis.imshow(
            grad,
            cmap="apolBarGrad",
            extent=[x, x + w, y, y + h],
            aspect="auto",
            zorder=1,
        )

    axis.set_xlim(xlim)
    axis.set_ylim(ylim)

    axis.grid(axis="y")

    return axis


def hbarplot_round(plotdata, categorical=False):

    """
    hbarplot_round

    As with hbarplot, except the bars are bevelled. If the bars represent
    categories, the default palette is used. If they do not, then you can
    instead plot all bars the same color, with a nice gradient fill.

    INPUTS:
        data - pandas Series for plotting

    KEYWORDS:
        categorical = False - if True, plot bars using to default palette

    OUTPUTS:
        axis - matplotlib axis object
    """

    data = plotdata.iloc[::-1]  # reverse order

    fig, axis = plt.subplots()

    # we want the bar to have a normal aspect ratio, otherwise the rounding fails
    h = 10 ** np.floor(np.log10(data.max()))

    # base the rounding size on bar aspect ratio
    rounding_size = (h * data.max() * 5 / data.size) ** 0.5 / 16

    padding = 0.3
    clipbox_width = 1.1 * data.max() + padding

    grad = np.atleast_2d(np.linspace(0, 1, 256))

    counter = 0

    yticks = []
    yticknames = []

    for barname, value in data.iteritems():

        w = value
        y = counter * 2 * h

        bar_extent = [0, w, y, y + h]

        yticks.append(counter * 2 * h + h / 2)
        yticknames.append(barname)
        counter += 1

        # create the underlying bar
        if categorical:
            next_color = np.array([[apolPaletteRGB[counter]]])
            im = axis.imshow(next_color, extent=bar_extent, aspect="auto", zorder=1)
        else:
            im = axis.imshow(
                grad, cmap="apolBarGrad", extent=bar_extent, aspect="auto", zorder=1
            )

        # round the edges by clipping them
        boxstyle = mpl.patches.BoxStyle(
            "round", pad=padding, rounding_size=rounding_size
        )

        fancybox = mpl.patches.FancyBboxPatch(
            (-clipbox_width + w - 2 * padding, y + padding),
            width=clipbox_width,
            height=h - 2 * padding,
            transform=axis.transData,
            boxstyle=boxstyle,
        )

        im.set_clip_path(fancybox)

    axis.set_yticks(yticks)
    axis.set_yticklabels(yticknames)

    axis.set_xlim(0, data.max() * 1.1)
    axis.set_ylim(-h / 2, counter * 2 * h)

    axis.grid(axis="y")

    return axis


def heatmap(data):

    """
    heatmap

    Convenience function, thin wrapper around sns.heatmap that sets
    cmap to "apol" and tick rotations to 45 (x) and 0 (y). If you
    don't want these defaults then use sns.heatmap directly.

    INPUTS:
        data - pandas DataFrame

    OUTPUTS:
        axis - matplotlib axis object

    """

    axis = sns.heatmap(data, cmap="apol")

    axis.tick_params(axis="x", rotation=45)
    axis.tick_params(axis="y", rotation=0)

    return axis
