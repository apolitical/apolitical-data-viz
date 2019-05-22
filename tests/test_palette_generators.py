import pytest
import numpy as np
import pandas as pd

from apol_dataviz.palette_generators import apol_teal_pal, apol_navy_pal


def test_apol_teal_pal():
    assert len(apol_teal_pal(N=5)) == 5


def test_apol_navy_pal():
    assert len(apol_navy_pal(N=3)) == 3
