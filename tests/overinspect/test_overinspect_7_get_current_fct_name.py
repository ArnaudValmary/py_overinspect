from overinspect.internal import i2__get_current_fct_name, i__get_current_fct_name

from pyoverinspect.overinspect import get_current_fct_name


def test_get_current_fct_name() -> None:
    assert get_current_fct_name() == 'test_get_current_fct_name'


def test_get_current_fct_name_level_2() -> None:
    assert i__get_current_fct_name(level=2) == 'test_get_current_fct_name_level_2'


def test_get_current_fct_name_level_3() -> None:
    assert i2__get_current_fct_name(level=3) == 'test_get_current_fct_name_level_3'
