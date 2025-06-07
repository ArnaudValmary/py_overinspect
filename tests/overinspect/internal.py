import os

from pyoverinspect.overinspect import (
    get_current_fct_filename,
    get_current_fct_line,
    get_current_fct_name,
)


def fct_without_param() -> None:
    pass


def fct_with_one_param(param: None) -> None:
    pass


def fct_with_two_params(param1: None, param2: None) -> None:
    pass


class ClassTest():
    def method(self) -> None:
        pass

    def method_bis(self, param: None) -> None:
        pass


def i__get_current_fct_filename(level: int = 1) -> str:
    return '/'\
        .join(
            get_current_fct_filename(level=level)
            .split(os.path.sep)
            [-4:]
        )


def i2__get_current_fct_filename(level: int = 1) -> str:
    return i__get_current_fct_filename(level=level)


def i__get_current_fct_line(level: int = 1) -> int:
    return get_current_fct_line(level=level)


def i2__get_current_fct_line(level: int = 1) -> int:
    return i__get_current_fct_line(level=level)


def i__get_current_fct_name(level: int = 1) -> str:
    return get_current_fct_name(level=level)


def i2__get_current_fct_name(level: int = 1) -> str:
    return i__get_current_fct_name(level=level)
