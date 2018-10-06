[![Buid Status][build]][travis] [![Code Coverage][cov]][codecov] [![Documentation Status][doc]][readthedocs] [![License Information][license]][mit]

[build]: https://travis-ci.org/caianrais/dora.svg?branch=master
[cov]: https://codecov.io/gh/caianrais/dora/branch/master/graph/badge.svg
[doc]: https://readthedocs.org/projects/dora/badge/?version=latest
[license]: https://img.shields.io/github/license/caianrais/dora.svg

[travis]: https://travis-ci.org/caianrais/dora
[codecov]: https://codecov.io/gh/caianrais/dora
[readthedocs]: https://dora.readthedocs.io
[mit]: https://github.com/caianrais/dora/blob/master/LICENSE


# DORA: DNS Over REST API

`DORA` is a microservice that provides a simple API for DNS querying through a
REST architecture. It aims to be a consumable API that's easy to digest and
easy to deploy on cloud-based solutions, such as [AWS Lambda][lambda], [GCP
Cloud Functions][gcp-cloud-func], [GCP AppEngine][gcp-app-engine],
[Heroku][heroku] and so on.

<p align="center">
    <img src="docs/example.png">
</p>

[lambda]: https://aws.amazon.com/lambda/
[gcp-cloud-func]: https://cloud.google.com/functions/
[gcp-app-engine]: https://cloud.google.com/appengine/
[heroku]: https://www.heroku.com/


## Features

`DORA` mainly relies on the [`dnspython`][dnspython] toolkit. It can query the
following records:

- `A`: IPv4 address;
- `AAAA`: IPv6 address;
- `CNAME`: Canonical name (name alias);
- `MX`: Mail exchange (mail transfer agent name);
- `NS`: Authoritative name server;
- `TXT`: Text records.

[dnspython]: https://github.com/rthalley/dnspython


## Documentation

For instructions of usage, installation, deployment and overall documentation
of the code, [read the docs](http://dora.rtfd.io).


## TODO

- [ ] Finish the user documentation;
- [ ] Create code documentation;
- [ ] 100% covered (*write tests*);
- [ ] Publish DORA on PyPI;
- [ ] Dockerized DORA;
- [ ] Guide: Deploying DORA on Heroku;
- [ ] Guide: Deploying DORA on AWS Lambda;
- [ ] Guide: Deploying DORA on Google App Engine;
- [ ] Guide: Deploying DORA on Google Cloud Functions;
