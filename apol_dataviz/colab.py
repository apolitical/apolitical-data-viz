import os
import sys

from requests import get
from zipfile import ZipFile

def download_lato_font(verbose=False):

    RUNNING_IN_COLAB = "google.colab" in sys.modules

    if not RUNNING_IN_COLAB:
        if verbose:
            print(
                """
                Not running in Google Colab. For best results ensure you have
                the Lato font installed on your system.
                """
            )
        return

    # if we are running in Google Colab, we need to install the correct font:
    mpl_fonts = "/usr/local/lib/python3.6/dist-packages/matplotlib/mpl-data/fonts/ttf/"
    lato_url = "https://www.1001freefonts.com/d/5722/lato.zip"

    if verbose:
        print("Downloading Lato font from {} ...".format(mpl_fonts))

    with open("lato.zip", "wb") as handle:
        handle.write(get(lato_url).content)

    if verbose:
        print("... extracting lato.zip contents to mpl-data/fonts ...")

    with ZipFile("lato.zip", "r") as zip:
        zip.extractall(mpl_fonts)

    if verbose:
        print("... cleaning up ...")

    os.remove("lato.zip")
    os.remove(mpl_fonts + "OFL.txt")

    if verbose:
        print("... complete.")
    
