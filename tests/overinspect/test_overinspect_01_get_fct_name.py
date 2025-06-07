from overinspect.internal import ClassTest, fct_without_param

from pyoverinspect.overinspect import FULL_QUAL, get_fct_name


def test_get_fct_name() -> None:
    assert get_fct_name(fct_without_param) == "fct_without_param"


def test_get_fct_name_method_() -> None:
    assert get_fct_name(ClassTest.method) == "method"


def test_get_fct_name_method_full_qual() -> None:
    assert get_fct_name(ClassTest.method, FULL_QUAL) == "ClassTest.method"
