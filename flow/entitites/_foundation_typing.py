from typing import Protocol as _Protocol


class Middleware(_Protocol):
    def handle(self) -> None:
        pass

    def __init__(self) -> None:
        super().__init__()
