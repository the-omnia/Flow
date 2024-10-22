from flow.entitites.http import HttpServer


def main() -> int:
    http_srv = HttpServer("", "")
    http_srv.setup()
    http_srv.serve()

    return 0


if __name__ == "__main__":
    exit(main())
