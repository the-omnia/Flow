__all__ = ("Middleware",)


from abc import ABC as _ABC
from abc import abstractmethod as _abstractmethod
from typing import final as _final


class Middleware(_ABC):
    @_abstractmethod
    def handle(self) -> None:
        pass

    @_final
    def __init__(self, name: str) -> None:
        pass
