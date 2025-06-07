import os

from overinspect.internal import ClassTest, fct_without_param

from pyoverinspect.overinspect import BUILTIN_FUNCTION, get_fct_filename


def test_get_fct_filename() -> None:
    assert '/'\
        .join(
            get_fct_filename(fct_without_param)
            .split(os.path.sep)
            [-4:]
        ) == \
        "py_overinspect/tests/overinspect/internal.py"


def test_get_fct_filename_method() -> None:
    assert '/'\
        .join(
            get_fct_filename(ClassTest.method)
            .split(os.path.sep)
            [-4:]
        ) == \
        "py_overinspect/tests/overinspect/internal.py"


def test_get_fct_filename_built_in() -> None:
    assert get_fct_filename(str) == BUILTIN_FUNCTION
