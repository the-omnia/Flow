"""Worker class implementation."""

__all__ = ("Worker",)

from typing import TYPE_CHECKING as __TYPE_CHECKING__


if __TYPE_CHECKING__:
    from typing import Any


class Worker:
    """Class which is responsible for dependency injection and runtime state.

    Since:
        0.1.0

    Version:
        0.1.0

    Authors:
        * Mark Sorokin
    """

    def run(self) -> None:
        pass

    def __init__(self, dependencies: list["Any"]) -> None:
        self.__dependencies__ = dependencies
