import pytest

from apol_dataviz import colors

@pytest.fixture
def color_definitions():
    return colors.ColorDefinitions()

def test_it_has_a_palette(color_definitions):
    assert hasattr(color_definitions, "apol_palette")

def test_it_has_a_color_lookup(color_definitions):
    assert hasattr(color_definitions, "apol_color_lookup")
