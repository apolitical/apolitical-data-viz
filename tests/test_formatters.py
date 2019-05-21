import pytest
import numpy as np
import pandas as pd

from apol_dataviz.formatters import get_ts_tick_labels

@pytest.fixture
def test_series():
    return pd.Series(
        np.random.randn(91),
        index=pd.date_range(start="2019-01-01", end="2019-04-01", freq="d"),
    )

def test_get_ts_tick_labels(test_series):
    xlab = get_ts_tick_labels(test_series)
    assert xlab.size == 91
