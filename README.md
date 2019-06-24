# apolitical-data-viz

This module defines the Apolitical (https://apolitical.co) 'house style' for data visualisation and provides various tools for plotting data. It is intended to be compatible with Google Colab.

We build heavily upon the foundations of [matplotlib](https://matplotlib.org/) and utilities provided by [seaborn](https://seaborn.pydata.org/), and aim for compatibility with [pandas](https://pandas.pydata.org/).

## Installation

To install from the command line via [pip](https://pip.pypa.io/en/stable/), do:

`pip install apolitical-data-viz`

To upgrade to the latest version via `pip` do:

`pip install apolitical-data-viz --upgrade`

To use via [pipenv](https://docs.pipenv.org/en/latest/) put the following in your Pipfile:

```
[packages]
apolitical-data-viz = ">=1.0.0"
```

## Development

If you've cloned the repository, the best way to make it work is using `pipenv`

If you don't yet have `pipenv`, you can use `pip` to install it from the command line:

`pip install pipenv --upgrade`

Then, in the top level directory of this repository, `apolitical-data-viz`, do:

`pipenv install --dev`

This will create the virtual environment and install the requirements (viewable in the Pipfile). The `--dev` flag will install packages needed for testing etc.

## Usage

To import the module, do the following:

`import apol_dataviz`

or e.g.

`import apol_dataviz as adv`

This provides a variety of resources (they can also be imported separately, as demonstrated in the next example).

### Applying the house style

The simplest usage is to simply enforce the house style. In order to do this, do the following:

```
from apol_dataviz import style
style.use_apol_style()
```

This will create a number of new matplotlib colour aliases as well as some new named colourmaps. Note that if you are using Google Colab, we anticipate that the Lato font will be missing and so we download the relevant `.ttf` files. This functionality relies on a check that `google-colab` is in the `sys.modules` list. If it is not, nothing is downloaded (you should ensure the Lato font is installed in your local `<PATH>/matplotlib/mpl-data/fonts/ttf/` directory in this case, else matplotlib will fall back on the default font).

### Accessing the colour definitions

If you don't want to enforce the full style, but do want to access our colour definitions, do the following:

```
from apol_dataviz.colours import ColourDefinitions

cd = ColourDefinitions()

cd.apply_definitions() # this command sets up the matplotlib aliases
```

The `ColourDefinitions` class contains the definitions of a wide variety of colours used in our visualisations. Its `apply_definitions()` method sets up the aliases for these in matplotlib.

### Using the custom plot utilities

We provide a number of different functions for plotting custom charts. These are accessible via the `plots` resource. These are intended to be compatible with pandas Series and DataFrames

```
from apol_dataviz.plots import doughnut, hbarplot

axis = doughnut(pandas_series)
axis = hbarplot(pandas_series)
```
The above commands would make nicely formatted doughnut (donut) plots and horizontal bar plots respectively.

### Formatting plots

In many cases we may want to format a plot in a particular way, and for this purpose we provide formatters that either alter the formatting of a particular plot or act as a utility for doing so.

As an example:

```
from apol_dataviz import formatters

new_tick_labels = formatters.get_ts_tick_labels(pandas_timeseries)
```

This creates well-formatted tick labels for a datetime-indexed pandas time series.

### Using the palette generators

We make available a number of functions for generating palettes of specific types.

To give a couple of examples:

```
from apol_dataviz import palette_generators as palgen

easy_sequential = palgen.apol_teal_pal()

categorical_via_HuSL = palgen.spaced_hue_palette()
```
