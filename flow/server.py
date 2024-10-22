from enum import Enum as _enum
from multiprocessing.pool import ThreadPool as _ThreadPool
from typing import TYPE_CHECKING as __TYPE_CHECKING__
from pathlib import Path as _Path

from .buildin import RunState as _RunState
from .buildin import WarmUpState as _WarmUpState

from .foundation import StateMachine as _StateMachine
from .foundation import Worker as _Worker

from .worker import FlowWorker as _FlowWorker


if __TYPE_CHECKING__:
    from .configuration import Configuration


class FlowServerState(_enum):
    startup = "startup"
    working = "working"
    shutdown = "shutdown"


class FlowServer:
    """Root runtime controller.

    Since:
        0.1.0

    Version:
        0.1.0

    Authors:
        * Mark Sorokin
    """

    def execute(self, dsn: str) -> None:
        """Start server.

        Function will start server process and start all internal handlers of any kind of protocol. In several
        cases will provide additional traceback which might be useful for developers, in production mode it is
        dumped.

        See:
            https://docs.the-omnia.ru/flow/configuration/root

        Params:
            * dsn - String, dsn of server
        """
        self.__state__ = FlowServerState.working
        self.__workers__.append(
            _FlowWorker(
                0,
                self.__thread_pool__,
                None,
                self.__tcp_socket__,
                [],
            )
        )

        while self.__state__ == FlowServerState.working:
            pass

        try:
            self.__state_machine__.switch("warm-up")
            self.__state_machine__.switch("run")

        except Exception as e:
            raise e

        finally:
            self.__state_machine__.switch("shutdown")
            self.shutdown()

    def enable_http(self) -> None:
        pass

    def add_worker(self, worker: _Worker) -> None:
        """Add new worker to server."""
        pass

    def shutdown(self) -> None:
        """Gracefully shutdown server."""

    def __init__(self, root_configuration: str) -> None:
        conf_path = _Path(root_configuration)

        self.__home_path__ = conf_path.parent
        try:
            self.__configurations__ = self.__load_configurations__()
            self.__state_machine__ = self.__init_state_machine__()
            self.__workers__: list[_Worker] = []

        except Exception as e:
            raise e

    def __load_configurations__(self) -> "list[Configuration]":
        return []

    def __init_state_machine__(self) -> _StateMachine:
        sm = _StateMachine()

        sm.register(_WarmUpState())
        sm.register(_RunState())

        return sm
