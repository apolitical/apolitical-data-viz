# colors.py - color definitions for style

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

plt.ion()
import seaborn as sns

sns.set_color_codes()


class ColorDefinitions:

    blueTeal = "#00B3BF"
    shockPink = "#ED1F7A"
    strongPurple = "#6B3ECD"
    paleOrange = "#FF7550"
    mintGreen = "#5ECE8A"
    goldenYellow = "#FCCA4C"
    plotGrey = "#B7C5D5"
    navyBlue = "#081D48"
    brightBlue = "#1772B8"
    strongRed = "#DC3C43"
    greenTeal = "#46B8A6"
    lightPurple = "#B75BB4"

    whiteTeal = "#EBF6F7"
    chartLabels = "#565A5C"
    chartDemarcation = "#081D48"  # 0.2 alpha for borders, 0.08 for gridlines

    apol_palette = [
        blueTeal,
        navyBlue,
        shockPink,
        plotGrey,
        strongPurple,
        paleOrange,
        mintGreen,
        goldenYellow,
        brightBlue,
        strongRed,
        greenTeal,
        lightPurple,
    ]

    apol_color_lookup = {
        "blueTeal": "#00B3BF",
        "navyBlue": "#081D48",
        "shockPink": "#ED1F7A",
        "plotGrey": "#B7C5D5",
        "strongPurple": "#6B3ECD",
        "paleOrange": "#FF7550",
        "mintGreen": "#5ECE8A",
        "goldenYellow": "#FCCA4C",
        "brightBlue": "#1772B8",
        "strongRed": "#DC3C43",
        "greenTeal": "#46B8A6",
        "lightPurple": "#B75BB4",
        "whiteTeal": "#EBF6F7",
        "blueTealComplement": "#D3EBEE",
        "navyBlueComplement": "#E8E9ED",
        "chartLabels": "#565A5C",
        "chartDemarcation": "#081D48",
    }

    def __init__(self):

        """
        __init__ for ColorDefinitions

        Adds matplotlib aliases for colors, registers colormaps

        """

        # convert the palette into alternative RGB format
        self.make_rgb_palette()
        # chart borders should have transparency:
        self.chartBordersRGBA = sns.external.husl.hex_to_rgb(
            self.cget("chartDemarcation")
        )
        # set the transparency to 0.80 (alpha=0.20)
        self.chartBordersRGBA.append(0.20)

    def apply_definitions(self):

        """
        apply_definitions

        This method wraps calls to .generate_aliases and .generate_cmaps.
        Calling it will update the matplotlib definitions to use the
        colors and palettes associated with this class

        """

        # set up matplotlib aliases for our colors
        self.generate_aliases()
        # create colormaps and register them with matplotlib
        self.generate_cmaps()

    def show_palette(self):

        """
        show_palette

        Invokes sns.palplot on self.apol_palette

        """

        sns.show_palette(self.apol_palette)

    @staticmethod
    def add_color_alias(cname, hexcode):

        """
        _add_color_alias

        This static method adds an alias for custom colors in
        matplotlib plotting methods via a string designation

        INPUTS:
            cname - name for the color
            hexcode - definition for the color

        """

        rgb = mpl.colors.colorConverter.to_rgb(hexcode)

        mpl.colors.colorConverter.colors[cname] = rgb
        mpl.colors.colorConverter.cache[cname] = rgb

    @staticmethod
    def cmap_between(hexcode1, hexcode2):

        """
        cmap_between

        This static method returns a ListedColormap between two extremal values

        INPUTS:
            hexcode1, hexcode2 - two names of known

        OUTPUTS:
            cmap - ListedColormap

        """

        gradientRGB1 = sns.external.husl.hex_to_rgb(hexcode1)
        gradientRGB2 = sns.external.husl.hex_to_rgb(hexcode2)

        n_seg = 256
        cmap_gradient = np.ones((n_seg, 4))

        for i, c in enumerate("RGB"):
            cmap_gradient[:, i] = np.linspace(gradientRGB1[i], gradientRGB2[i], n_seg)

        return mpl.colors.ListedColormap(cmap_gradient)

    def cget(self, color_name):

        """
        cget

        Convenience method: looks up a color in the definitions dict and
        returns the appropriate hexcode

        """

        return self.apol_color_lookup.get(color_name)

    def generate_aliases(self):

        """
        generate_aliases

        This method registers all colors in .apol_color_lookup with
        matplotlib so that they can be used in plotting methods directly

        """

        for cname, hexcode in self.apol_color_lookup.items():
            self.add_color_alias(cname, hexcode)

    def generate_cmaps(self):

        """
        generate_cmaps

        This method generates two color maps and registers them under

            apol (whiteTeal <--> blueTeal)
            apolBarGrad (greenTeal <--> blueTeal)

        The ListedColormap objects themselves are accessible at

            .apolCM
            .barGradientCM

        """

        self.apolCM = self.cmap_between(self.cget("whiteTeal"), self.cget("blueTeal"))

        self.barGradientCM = self.cmap_between(
            self.cget("greenTeal"), self.cget("blueTeal")
        )

        # register these colormaps
        mpl.cm.register_cmap(name="apol", cmap=self.apolCM)
        mpl.cm.register_cmap(name="apolBarGrad", cmap=self.barGradientCM)

    def make_rgb_palette(self):

        """
        make_rgb_palette

        This method sets the attribute .apol_paletteRGB, which is created
        from .apol_palette, a list of hexcodes. Sometimes the RGB format
        is easier to work with

        """

        self.apol_paletteRGB = [
            sns.external.husl.hex_to_rgb(hexcode) for hexcode in self.apol_palette
        ]
