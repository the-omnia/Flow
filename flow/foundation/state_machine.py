"""Implementation of StateMachine class."""

__all__ = (
    "State",
    "StateHandler",
    "StateMachine",
)


from abc import ABC as _ABC
from abc import abstractmethod as _abstractmethod
from typing import TYPE_CHECKING as __TYPE_CHECKING__
from typing import final as _final


if __TYPE_CHECKING__:
    from typing import Any

    from .worker import Worker


class State(_ABC):
    @property
    @_abstractmethod
    def requires(self) -> list[str]:
        raise NotImplementedError('property "requires" does not implemented')

    @_abstractmethod
    def handle(self) -> None:
        pass

    @_abstractmethod
    def setup_handler(self, args: list["Any"]) -> None:
        raise NotImplementedError('method "setup_handlers" does not implemented')

    @_final
    def __init__(self) -> None:
        super().__init__()


class StateHandler(_ABC):
    @_abstractmethod
    def handle(self) -> None:
        """Handle state if required."""

    def __init__(self, name: str, elements: list) -> None:
        pass


class StateMachine:
    """Root controller of state inside runtime.

    State machine is representation of internal runtime, which might be handy when need to perform some quirky
    or runtime things. Instead of Spring Boot implementation, where state machine is provided in different
    package and needed to be added manually, Flow provides it out of the box.

    From the beginning it has this states: warmup, running, shutting-down. You may connect to each of them or
    add custom one with `flow.foundation.State` class. After filling your required needs, use following code:

    >>> from flow.foundation import State
    ... from flow.foundation import StateMachine
    ...
    ... class MyState(State):
    ...     @property
    ...     def requires(self) -> list[str]:
    ...         return ['list of elements that will be needed']
    ...
    ...     def handle(self) -> None:
    ...         # handle your state
    ...
    ...     def setup_handlers(self) -> None:
    ...         # init your handlers here
    ...
    ...
    ... sm = StateMachine()
    ... sm.register(MyState, "my-state")

    Following code will register state in the end, but if you want to add it before something else then:

    >>> sm.register_before("running", MyState, "my-state")

    To perform switch, simply call method `switch`

    >>> sm.switch("my-state")

    Since:
        0.1.0

    Version:
        0.1.0

    Authors:
        * Mark Sorokin
    """

    @property
    def current(self) -> State:
        return self.__states__[0]

    @property
    def states(self) -> list[State]:
        return self.__states__

    def register(self, state: State) -> None:
        """Register new state.

        Params:
            * state - `flow.foundation.State`, object, which will be injected with required dependencies

        Since:
            0.1.0

        Version:
            0.1.0
        """

    def switch(self, name: str) -> None:
        pass

    def __init__(self) -> None:
        self.__states__: list[State] = []
