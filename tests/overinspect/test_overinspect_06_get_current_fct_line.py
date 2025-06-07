from overinspect.internal import i2__get_current_fct_line, i__get_current_fct_line

from pyoverinspect.overinspect import get_current_fct_line


def test_get_current_fct_line() -> None:
    assert get_current_fct_line() == 7


def test_get_current_fct_line_level_2() -> None:
    assert i__get_current_fct_line(level=2) == 11


def test_get_current_fct_line_level_3() -> None:
    assert i2__get_current_fct_line(level=3) == 15
