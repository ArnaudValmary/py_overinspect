
from overinspect.internal import (
    ClassTest,
    fct_with_one_param,
    fct_with_two_params,
    fct_without_param,
)

from pyoverinspect.overinspect import get_fct_parameter_names


def test_get_fct_parameter_names_0() -> None:
    assert get_fct_parameter_names(fct_without_param) == []


def test_get_fct_parameter_names_1() -> None:
    assert get_fct_parameter_names(fct_with_one_param) == ['param']


def test_get_fct_parameter_names_2() -> None:
    assert get_fct_parameter_names(fct_with_two_params) == ['param1', 'param2']


def test_get_fct_parameter_names_method() -> None:
    assert get_fct_parameter_names(ClassTest.method) == ['self']


def test_get_fct_parameter_names_method_2() -> None:
    assert get_fct_parameter_names(ClassTest.method_bis) == ['self', 'param']
