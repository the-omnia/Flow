__all__ = ("FlowWorker",)

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from logging import Logger
    from multiprocessing.pool import ThreadPool
    from socket import socket


class FlowWorker:
    """General server worker.

    Worker class provides general functionality for handling requests from incoming clients. It contains all
    middlewares, routing and error handling which is required for working with request/response model. Workers
    comes as load-balancers and performance elements, which further optimizes requests using cached values.

    Authors
    -------
    * Mark Sorokin <assertionbit@icloud.com>

    License
    -------
    Omnia Closed Source License version 1

    Copyright
    ---------
    Omnia community 2024

    Since
    -----
    0.1.0

    Version
    -------
    """

    def execute(self) -> None:
        while self.__execute__:
            for request in self.__requests__:
                try:
                    self.handle()
                except:
                    pass

    def handle(self) -> None:
        pass

    def shutdown(self) -> None:
        """Graceful shutdown worker"""

    def __init__(
        self,
        id: int,
        thread_pool: "ThreadPool",
        logger: "Logger",
        tcp_socket: "socket",
        # middlewares: list[Middleware],
    ) -> None:
        self.__worker_id__ = id
        self.__logger__ = logger
        self.__thread_pool__ = thread_pool
        self.__tcp_socket__ = tcp_socket
        # self.__middlewares__ = middlewares
        self.__execute__ = False
        self.__requests__: list[str] = []
