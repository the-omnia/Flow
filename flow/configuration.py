from abc import ABC as _ABC
from abc import abstractmethod as _abstractmethod
from typing import TYPE_CHECKING as __TYPE_CHECKING__
from typing import final as _final
from inspect import getmembers as _getmembers
from inspect import ismethod as _ismethod
from inspect import ismethodwrapper as _ismethodwrapper


if __TYPE_CHECKING__:
    from typing import Any
    from pathlib import Path


class Configuration(_ABC):
    @property
    def configPath(self) -> "Path":
        return self.__config_path__

    @_abstractmethod
    def load(self) -> "Any":
        """Load configuration from specific file."""
        raise NotImplementedError("method 'Configuration.load' is not implemented")

    @_final
    def __init__(self, path: "Path") -> None:
        super().__init__()
        self.__config_path__ = path
        self.__read_properties__()

    @_final
    def __read_properties__(self) -> None:
        methods = _getmembers(self, predicate=_ismethod)
