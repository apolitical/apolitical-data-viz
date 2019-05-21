# Please note: these functions only work properly if the colour definitions have been set.
# Therefore be aware that importing these functions has that side-effect.
import seaborn as sns

from apol_dataviz.colours import ColourDefinitions

hex2husl = sns.external.husl.hex_to_husl
husl2hex = sns.external.husl.husl_to_hex

cd = ColourDefinitions()
cd.apply_definitions()

def apol_teal_pal(N=4, reverse=False):

    """
    apol_teal_pal

    Function that gets a sequential palette in blueTeal

    KEYWORDS:
        N = 4 - return 4 sequential colours unless specified
        reverse = False - light to dark unless true

    OUTPUTS:
        palette - list of hexcodes as strings
    """

    pale = cd.cget("blueTealComplement")
    dark = cd.cget("blueTeal")

    pair = [pale, dark] if not reverse else [dark, pale]
    return sns.palettes.blend_palette(pair, N)

def apol_navy_pal(N=4, reverse=False):

    """
    apol_navy_pal

    Function that gets a sequential palette in navyBlue

    KEYWORDS:
        N = 4 - return 4 sequential colours unless specified
        reverse = False - light to dark unless true

    OUTPUTS:
        palette - list of hexcodes as strings

    """

    pale = cd.cget("navyBlueComplement")
    dark = cd.cget("navyBlue")

    pair = [pale, dark] if not reverse else [dark, pale]
    return sns.palettes.blend_palette(pair, N)

def spaced_hue_palette(n_col=5, base_colour=cd.blueTeal):

    """
    spaced_hue_palette

    The HuSL system is a neat way of creating colour palettes that have a
    uniform apparent brightness. This function returns such a palette
    that includes one chosen colour. The colours are evenly spaced in
    hue by default.

    KEYWORDS:
        n_col = 5 - number of colours to have in the palette
        base_colour = cd.blueTeal - starting point for palette generation

    OUTPUTS:
        hexcodes - list of colour hexcodes comprising a palette

    """

    # convert base_colour hexcode -> HuSL representation
    H, S, L = hex2husl(base_colour)

    hues = np.linspace(0, 360, n_col, endpoint=False)

    hues += H

    hexcode_generator = map(lambda h: husl2hex(h, S, L), hues)

    hexcodes = [hexcode for hexcode in hexcode_generator]

    return hexcodes

def spaced_saturation_palette(n_col=5, base_colour=cd.blueTeal):

    """
    spaced_saturation_palette

    Returns a list (palette) of colours evenly spaced in saturation,
    interpolating through a base colour

    KEYWORDS:
        n_col = 5 - number of colours to have in the palette
        base_colour = cd.blueTeal - starting point for palette generation

    OUTPUTS:
        hexcodes - list of colour hexcodes comprising a palette

    """

    # convert base_colour hexcode -> HuSL representation
    H, S, L = hex2husl(base_colour)

    sats = np.linspace(0, 100, n_col)

    hexcode_generator = map(lambda s: husl2hex(H, s, L), sats)

    hexcodes = [hexcode for hexcode in hexcode_generator]

    return hexcodes

def spaced_lightness_palette(n_col=5, base_colour=cd.blueTeal):

    """
    spaced_lightness_palette

    Returns a list (palette) of colours evenly spaced in lightness,
    interpolating through a base colour

    KEYWORDS:
        n_col = 5 - number of colours to have in the palette
        base_colour = cd.blueTeal - starting point for palette generation

    OUTPUTS:
        hexcodes - list of colour hexcodes comprising a palette

    """

    # convert base_colour hexcode -> HuSL representation
    H, S, L = hex2husl(base_colour)

    lis = np.linspace(0, 100, n_col)

    hexcode_generator = map(lambda l: husl2hex(H, S, l), lis)

    hexcodes = [hexcode for hexcode in hexcode_generator]

    return hexcodes

def spaced_brightness_palette(n_col=5, base_colour=cd.blueTeal):

    """
    spaced_brightness_palette

    Returns a list (palette) of colours evenly spaced in lightness
    and saturation, interpolating through a base colour

    KEYWORDS:
        n_col = 5 - number of colours to have in the palette
        base_colour = cd.blueTeal - starting point for palette generation

    OUTPUTS:
        hexcodes - list of colour hexcodes comprising a palette

    """

    # convert base_colour hexcode -> HuSL representation
    H, S, L = hex2husl(base_colour)

    lisats = np.linspace(0, 100, n_col)

    hexcode_generator = map(lambda x: husl2hex(H, x, x), lisats)

    hexcodes = [hexcode for hexcode in hexcode_generator]

    return hexcodes

def opposing_hue_palette(n_col=5, base_colour=cd.blueTeal):

    """
    opposing_hue_palette

    Returns a diverging colour palette with a chosen base-colour on one
    end, its opposing, equal-apparent-brightness hue on the other (via
    the HuSL system), interpolating through white in the middle. This
    will always be the central hue of the palette if the number of
    colours in the palette is odd.

    KEYWORDS:
        n_col = 5 - number of colours to have in the palette
        base_colour = cd.blueTeal - starting point for palette generation

    OUTPUTS:
        hexcodes - list of colour hexcodes comprising a palette

    """

    # convert base_colour hexcode -> HuSL representation
    H, S, L = hex2husl(base_colour)

    H2 = H + 180

    colours_per_arm = n_col // 2

    require_midpoint = bool(n_col % 2) # do we need a midpoint?

    saturations = np.linspace(S, 100, colours_per_arm + 1)[:-1]
    lightnesses = np.linspace(L, 100, colours_per_arm + 1)[:-1]

    arm1 = zip([H]*colours_per_arm, saturations, lightnesses)
    arm2 = zip([H2]*colours_per_arm, saturations[::-1], lightnesses[::-1])

    arm1hex = [husl2hex(h,s,l) for h,s,l in arm1]
    arm2hex = [husl2hex(h,s,l) for h,s,l in arm2]

    if not require_midpoint:
        return arm1hex + arm2hex

    midhex = [husl2hex(H, 100, 100)]

    return arm1hex + midhex + arm2hex
