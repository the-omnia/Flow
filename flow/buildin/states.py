from typing import final as _final

from flow.foundation import State as _State


@_final
class WarmUpState(_State):
    @property
    def requires(self) -> list[str]:
        return [
            "@configurations",
            "@middlewares",
            "@workers",
        ]

    def handle(self) -> None:
        pass

    def setup_handlers(self) -> None:
        pass


@_final
class RunState(_State):
    @property
    def requires(self) -> list[str]:
        return ["@configurations", "@middlewares", "@workers"]

    def handle(self) -> None:
        pass

    def setup_handlers(self) -> None:
        pass
