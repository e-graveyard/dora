[![Buid Status][build]][travis] [![Code Quality][quality]][lgtm] [![Code Coverage][cov]][codecov] [![Documentation Status][doc]][readthedocs] [![License Information][license]][mit]

[build]: https://travis-ci.org/caiertl/dora.svg?branch=master
[quality]: https://img.shields.io/lgtm/grade/python/g/caiertl/dora.svg?logo=lgtm&logoWidth=18
[cov]: https://codecov.io/gh/caiertl/dora/branch/master/graph/badge.svg
[doc]: https://readthedocs.org/projects/dora/badge/?version=latest
[license]: https://img.shields.io/github/license/caiertl/dora.svg

[travis]: https://travis-ci.org/caiertl/dora
[lgtm]: https://lgtm.com/projects/g/caiertl/dora/context:python
[codecov]: https://codecov.io/gh/caiertl/dora
[readthedocs]: https://dora.readthedocs.io
[mit]: https://github.com/caiertl/dora/blob/master/LICENSE


# DORA: DNS over REST API

`DORA` is a microservice that provides a simple API for DNS querying through a
REST architecture. It aims to be a consumable API that's easy to digest and
easy to deploy on cloud-based solutions, such as [AWS Lambda][lambda] and
[Heroku][heroku].

<p align="center">
    <img src="docs/_static/example.png">
</p>

[lambda]: https://aws.amazon.com/lambda/
[heroku]: https://www.heroku.com/


## Features

`DORA` mainly relies on the [`dnspython`][dnspython] toolkit. It can query the
following records:

- `A`     : IPv4 address;
- `AAAA`  : IPv6 address;
- `CNAME` : Canonical name (name alias);
- `MX`    : Mail exchange (mail transfer agent name);
- `NS`    : Authoritative name server;
- `TXT`   : Text records.

[dnspython]: https://github.com/rthalley/dnspython


## Documentation

For instructions of usage, installation, deployment and overall documentation
of the code, [read the docs](http://dora.rtfd.io).


## Roadmap

- [ ] Finish the user documentation;
- [ ] Create code documentation;
- [ ] 100% covered (*write tests*);
- [X] Publish DORA on PyPI;
- [X] Dockerized DORA;
- [ ] Guide: Deploying DORA on Heroku;
- [ ] Guide: Deploying DORA on AWS Lambda;
