import os

from overinspect.internal import ClassTest, fct_without_param

from pyoverinspect.overinspect import (
    BUILTIN_FUNCTION,
    FULL_QUAL,
    get_full_fct_path_and_name,
)


def test_get_full_fct_path_and_name() -> None:
    assert '/'\
        .join(
            get_full_fct_path_and_name(fct_without_param)
            .split(os.path.sep)
            [-4:]
        ) == \
        "py_overinspect/tests/overinspect/internal.py.fct_without_param"


def test_get_full_fct_path_and_name_method() -> None:
    assert '/'\
        .join(
            get_full_fct_path_and_name(ClassTest.method)
            .split(os.path.sep)
            [-4:]
        ) == \
        "py_overinspect/tests/overinspect/internal.py.method"


def test_get_full_fct_path_and_name_method_full_qual() -> None:
    assert '/'\
        .join(
            get_full_fct_path_and_name(ClassTest.method, full_qual=FULL_QUAL)
            .split(os.path.sep)
            [-4:]
        ) == \
        "py_overinspect/tests/overinspect/internal.py.ClassTest.method"


def test_get_full_fct_path_and_name_method_sep() -> None:
    assert '/'\
        .join(
            get_full_fct_path_and_name(ClassTest.method, full_qual=FULL_QUAL, sep='#')
            .split(os.path.sep)
            [-4:]
        ) == \
        "py_overinspect/tests/overinspect/internal.py#ClassTest.method"


def test_get_full_fct_path_and_name_built_in() -> None:
    assert get_full_fct_path_and_name(str) == '%s.str' % BUILTIN_FUNCTION
