
<div align="center">
    <img src="icon.webp" width="216px">
    <h1>Omnia | Flow</h1>
    <i>General-purpose web framework with Spring Boot like experience for python</i>
</div>

> **Warning**
>
> Framework in early stage of development, consider waiting for first stable release.

**Flow** - [spring-boot](https://spring.io/) like framework for fully-featured web servers.
    Framework supports different kinds of connections: from simple http/1.0 to gRPC like connections.
    General usage of this framework is building production ready, safe and fast servers without need in
    adding new, unknown libraries, tools etc.

## Advantages

Flow might offer different kind of features that you might be interested.

### 1. Build-in web server

Many web frameworks rely on other kinds of execution runtime. But in this case: runtime is build-in. You 
    don't need in any additional items like [uvicorn](https://www.uvicorn.org/), [gunicorn](https://gunicorn.org/)
    etc. So all of features like monitoring, installing as service are already provided for You and waiting for
    some specific, small configurations.

### 2. Build-in logging/observability

Logging is important for production usage. You might want to observe what is going on inside inside of your server
    so all elements are prepared for you. Want to use external logger? You may without any kind of problem. Or you
    you want to use structured logging for [vector](https://vector.dev/) collector: do what you need. We also
    provide some plugins for [grafana]() or [zabbix](), so you there is no need in additional setups, after you 
    push it to production.

### 3. Fast and secure

There is no side dependencies, that may cause [supply-chain-attack](https://en.wikipedia.org/wiki/Supply_chain_attack).
    Build-in engine follows international RFC's for all kind of protocols, providing some additional features for
    you to configure your ideal runtime. Need to block some external connections, but need in FTP and don't want
    or could not install firewall, framework will help with that.

### And many more comes!

We will work on supporting more and more features, that will come as stable release, that will love and will use.

## Development

We working on this framework everyday. So any kind of support is best. Just reach out to us, contribution or use
    of this project is already huge support us. We don't accept any kind of financial support for now, but in
    future we planning to add some support for commercial use (like help with development, migrating, writting
    custom plugins etc.) to support other contributors of this project.

