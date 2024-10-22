__all__ = ("HttpHandler",)

from typing import final as _final

from flow.foundation import StateHandler as _Handler


@_final
class HttpHandler(_Handler):
    def handle(self) -> None:
        return super().handle()

    def __init__(self, name: str, elements: list) -> None:
        super().__init__(name, elements)
