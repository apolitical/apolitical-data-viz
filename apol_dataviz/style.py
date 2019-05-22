import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

plt.ion()
import seaborn as sns

sns.set_color_codes()

from apol_dataviz.colab import download_lato_font
from apol_dataviz.colors import ColorDefinitions


def use_apol_style():

    """
    use_apol_style

    This function sets up the Apolitical House Style for plotting

    """

    download_lato_font()  # takes no action if not running in a Google Colab notebook

    cd = ColorDefinitions()
    cd.apply_definitions()  # register colors and colormaps with matplotlib

    apol_labelsize = 16
    apol_titlesize = 18

    ## set up the defaults for plotting

    mpl.font_manager._rebuild()

    APOLITICAL_HOUSE_STYLE = {
        "axes.axisbelow": True,
        "axes.edgecolor": cd.chartBordersRGBA,
        "axes.facecolor": "white",
        "axes.grid": True,
        "axes.labelcolor": cd.chartLabels,
        "axes.labelweight": "bold",
        "axes.labelsize": apol_labelsize,
        "axes.prop_cycle": mpl.cycler(color=cd.apol_paletteRGB),
        "axes.spines.bottom": True,
        "axes.spines.left": True,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.titlesize": apol_titlesize,
        "axes.titleweight": "bold",
        "figure.edgecolor": cd.chartBordersRGBA,
        "figure.facecolor": "white",
        "figure.figsize": [10, 6],
        "font.sans-serif": ["Lato"],
        "font.weight": 100,
        "grid.alpha": 0.08,
        "grid.color": cd.chartDemarcation,
        "image.cmap": "apol",
        "lines.color": cd.chartBordersRGBA,
        "patch.edgecolor": cd.chartDemarcation,
        "text.color": cd.chartLabels,
        "xtick.bottom": False,
        "xtick.labelsize": apol_labelsize,
        "xtick.top": False,
        "ytick.labelsize": apol_labelsize,
        "ytick.left": False,
        "ytick.right": False,
    }

    plt.style.use("default")
    plt.style.use(APOLITICAL_HOUSE_STYLE)


if __name__ == "__main__":
    # if style.py is directly executed, set all the definitions
    use_apol_style()
    print("Now using the Apolitical House Style for matplotlib graphics.")
