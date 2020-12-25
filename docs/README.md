[![Buid Status][build]][travis] [![Code Quality][quality]][lgtm] [![Code Coverage][cov]][codecov] [![Documentation Status][doc]][readthedocs]

[build]: https://travis-ci.org/caian-org/dora.svg?branch=master
[quality]: https://img.shields.io/lgtm/grade/python/g/caian-org/dora.svg?logo=lgtm&logoWidth=18
[cov]: https://codecov.io/gh/caian-org/dora/branch/master/graph/badge.svg
[doc]: https://readthedocs.org/projects/dora/badge/?version=latest
[license]: https://img.shields.io/github/license/caian-org/dora.svg

[travis]: https://travis-ci.org/caian-org/dora
[lgtm]: https://lgtm.com/projects/g/caian-org/dora/context:python
[codecov]: https://codecov.io/gh/caian-org/dora
[readthedocs]: https://dora.readthedocs.io


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


## License

[![Kopimi Logo][kopimi-logo]][kopimi-url]

To the extent possible under law, [Caian Rais Ertl][me] has waived __all
copyright and related or neighboring rights to this work__. In the spirit of
_freedom of information_, I encourage you to fork, modify, change, share, or do
whatever you like with this project! `^C ^V`

[![License][cc-shield]][cc-url]

[me]: https://github.com/caiertl
[cc-shield]: https://forthebadge.com/images/badges/cc-0.svg
[cc-url]: http://creativecommons.org/publicdomain/zero/1.0

[kopimi-logo]: https://gist.githubusercontent.com/xero/cbcd5c38b695004c848b73e5c1c0c779/raw/6b32899b0af238b17383d7a878a69a076139e72d/kopimi-sm.png
[kopimi-url]: https://kopimi.com
