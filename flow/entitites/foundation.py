from abc import ABC as _ABC
from abc import abstractmethod as _abstractmethod
from typing import TYPE_CHECKING as __TYPE_CHECKING__
from typing import Type as _Type
from typing import final as _final


if __TYPE_CHECKING__:
    from ._foundation_typing import Middleware


class Client:
    """General information about client, which makes request.

    Since:
        0.1.0

    Version:
        0.1.0
    """

    @property
    @_abstractmethod
    def type(self) -> str:
        raise NotImplementedError('property "type" is not implemented')

    def __init__(self) -> None:
        pass


class Request(_ABC):
    """Base class for any kind of request"""

    @property
    def client(self) -> Client: ...

    def __init__(self) -> None:
        pass


class HttpResponse:
    @_abstractmethod
    def write(self, destination) -> None:
        pass


class Server(_ABC):
    """General interface for web server, which will handle all kind of requests.

    Since:
        0.1.0

    Version:
        0.1.0
    """

    @_abstractmethod
    def shutdown(self) -> None:
        pass

    @_abstractmethod
    def serve(self) -> None:
        pass

    @_abstractmethod
    def setup(self) -> None:
        """Perform setup of server for usage"""

    @_abstractmethod
    def add_middleware(self, middleware: "Middleware") -> None:
        pass

    def __init__(self, conf, dependencies) -> None:
        super().__init__()
        self.__configuration__ = conf
        self.__middlewares__: list["Middleware"] = []
