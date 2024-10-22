from typing import TYPE_CHECKING as __TYPE_CHECKING__
from typing import final as _final
from socket import AF_INET as _AF_INET
from socket import SOCK_STREAM as _SOCK_STREAM
from socket import socket as _socket

from .foundation import Client as _Client
from .foundation import Request as _Request
from .foundation import Server as _Server
from .middleware import Middleware as _Middleware


if __TYPE_CHECKING__:
    from typing import Any
    from socket import _RetAddress


class HttpHeader:
    @property
    def name(self) -> str:
        return self.__name__.decode()

    @property
    def value(self) -> str:
        return self.__value__.decode()

    def __init__(self, key: bytes, value: bytes) -> None:
        self.__name__ = key
        self.__value__ = value.strip(" ".encode())

    def __bytes__(self) -> bytes:
        return self.__name__ + ": ".encode() + self.__value__


@_final
class HttpClient(_Client):
    @property
    def method(self) -> str:
        return self.__method__

    @property
    def route(self) -> str:
        return self.__route__

    @property
    def version(self) -> str:
        return self.__version__

    @property
    def headers(self) -> list[HttpHeader]:
        return self.__headers__

    def __init__(self, soc: _socket, addr: "_RetAddress") -> None:
        self.__address__ = addr
        self.__socket__ = soc
        data = soc.recv(100)
        self.__parse_main_line__(data)
        self.__parse_headers__(data)

    def __parse_main_line__(self, data: bytes) -> None:
        header = data.split("\r\n".encode())[0]
        method, route, version = header.split(" ".encode())

        self.__method__ = method.decode()
        self.__route__ = route.decode()
        self.__version__ = version.replace("HTTP/".encode(), "".encode()).decode()

    def __parse_headers__(self, data: bytes) -> None:
        self.__headers__: list[HttpHeader] = []

        for header in data.split("\r\n".encode())[1:]:
            if header == "".encode():
                break

            h = header.split(": ".encode(), 1)
            self.__headers__.append(HttpHeader(h[0], h[1]))

    def __del__(self) -> None:
        self.__socket__.close()


class HttpMiddleware(_Middleware):
    def handle(self) -> None:
        pass


@_final
class HttpRequest(_Request):
    @property
    def method(self) -> str:
        return self.__method__.decode()

    @property
    def route(self) -> str:
        return self.__route__.decode()

    @property
    def version(self) -> int:
        try:
            return int(self.__version__.split(".".encode())[1].decode())

        except IndexError:
            return 1

        except ValueError:
            return 1

    @property
    def headers(self) -> list[HttpHeader]:
        return self.__headers__

    @property
    def client(self) -> HttpClient:
        return self.__client__  # type: ignore

    @property
    def content(self) -> str:
        return self.__content__.decode()

    def __init__(self, soc: _socket, addr: "_RetAddress") -> None:
        self.__socket__ = soc
        self.__address__ = addr
        data = soc.recv(1000).split("\r\n".encode())

        # Parsing entities of request
        self.__parse_main_line__(data.pop(0))
        self.__parse_headers__(data)
        self.__parse_body__(data)

        # self.__client__ = HttpClient(
        #    soc,
        #    addr,
        # )

    def __parse_main_line__(self, line: bytes) -> None:
        """Parse main line in HTTP request.

        Params:
            line - byte-like string, containing data in form of "<METHOD> <ROUTE> HTTP/<PROTOCOL-VERSION>"

        Since:
            0.1.0
        """

        self.__method__, self.__route__, self.__version__ = line.split(" ".encode())

        self.__version__ = self.__version__.removeprefix("HTTP/".encode())

    def __parse_headers__(self, lines: list[bytes]) -> None:
        """Parse headers of request.

        Method will parse all kind of headers and pass them into internal array, which further could be
            used for type detecting, cookie access and other things. For most, this does nothing to ensure
            that they are W3C standard compliant.

        Api-Note:
            For those, who will work with original data from __init__ method remember: this method uses
            lines array as queue for working with all of this, futher data after working with this element:
            may contain less data.

        Params:
            * lines - array[bytes], queue threated structure, from where data will be extracted.
        """

        self.__headers__: list[HttpHeader] = []

        while True:
            if len(lines) == 0:
                break

            if len(lines[0]) == 0:
                break

            header = lines.pop(0)
            key, value = header.split(":".encode(), maxsplit=1)
            self.__headers__.append(HttpHeader(key, value))

    def __parse_body__(self, lines: list[bytes]) -> None:
        self.__content__: bytes = bytes()

        if self.method == "GET":
            return

        # Handling non-empty content
        if len(lines) != 0:
            if len(lines[0]) == 0 and len(lines[1]) != 1:
                lines.pop(0)

        while True:
            if len(lines) == 0:
                return

            if len(lines[0]) == 0:
                return

            self.__content__ += lines.pop(0)

    def keys(self) -> list[str]:
        return ["protocol", "headers"]

    def __getitem__(self, key: str) -> "Any":
        return {
            "protocol": {
                "version": self.version,
                "method": self.method,
                "route": self.route,
            },
            "headers": dict(
                zip([h.name for h in self.headers], [h.value for h in self.headers])
            ),
        }[key]

    def __del__(self) -> None:
        self.__socket__.close()


@_final
class HttpServer(_Server):
    """Classis implementation of HTTP server.

    Version:
        0.1.0

    Since:
        0.1.0
    """

    def serve(self) -> None:
        while True:
            self.__tcp_socket__.listen()
            (con, addr) = self.__tcp_socket__.accept()
            client = HttpRequest(con, addr)

            con.send("Hello-World".encode())

            break

    def shutdown(self) -> None:
        self.__tcp_socket__.close()

    def setup(self) -> None:
        self.__tcp_socket__ = _socket(_AF_INET, _SOCK_STREAM)
        self.__tcp_socket__.bind(
            ("127.0.0.1", 8080),
        )

    def add_middleware(self, middleware: HttpMiddleware) -> None:  # type: ignore[override]
        """Add new HTTP middleware in general stack of middlewares.

        Method will add middleware to all routes that will be handled by this server. This will affect all handled
        routes including those, which will have it's own routing elements. This behavior is useful when want
        to cases, when you would like to handle some sort of end errors or add logging to your routing.
        Dependency injection in such cases is not required, due to all dependencies are possibly passed in
        init section.

        Params:
            * middleware - flow.entities.http.HttpMiddleware, instance of class, which further will be passed to
                           handling process.
        """

        self.__middlewares__.append(middleware)

    def __init__(self, conf, dependencies) -> None:
        super().__init__(conf, dependencies)
        self.__middlewares__: list[_Middleware] = []  # type: ignore[override]
