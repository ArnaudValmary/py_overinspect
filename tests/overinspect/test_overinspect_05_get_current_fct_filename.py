import os

from overinspect.internal import (
    i2__get_current_fct_filename,
    i__get_current_fct_filename,
)

from pyoverinspect.overinspect import get_current_fct_filename


def test_get_current_fct_filename() -> None:
    assert '/'\
        .join(
            get_current_fct_filename()
            .split(os.path.sep)
            [-4:]
        ) == \
        "py_overinspect/tests/overinspect/test_overinspect_05_get_current_fct_filename.py"


def test_get_current_fct_filename_level_2() -> None:
    assert i__get_current_fct_filename(2) == \
        "py_overinspect/tests/overinspect/test_overinspect_05_get_current_fct_filename.py"


def test_get_current_fct_filename_level_3() -> None:
    assert i2__get_current_fct_filename(3) == \
        "py_overinspect/tests/overinspect/test_overinspect_05_get_current_fct_filename.py"
