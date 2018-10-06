.. image:: https://travis-ci.org/caianrais/dora.svg?branch=master
        :target: https://travis-ci.org/caianrais/dora
        :alt: Build Status

.. image:: https://codecov.io/gh/caianrais/dora/branch/master/graph/badge.svg
        :target: https://codecov.io/gh/caianrais/dora
        :alt: Code Coverage Status

.. image:: https://readthedocs.org/projects/dora/badge/?version=latest
        :target: https://dora.readthedocs.io
        :alt: Documentation Status

.. image:: https://img.shields.io/github/license/caianrais/dora.svg
        :target: https://github.com/caianrais/dora/blob/master/LICENSE
        :alt: License Information


DORA: DNS Over REST API
=======================

``DORA`` is a microservice that provides a simple API for DNS querying through
a REST architecture. It aims to be a consumable API that's easy to digest and
easy to deploy on cloud-based solutions, such as `AWS Lambda`_, `GCP Cloud
Functions`_, `GCP AppEngine`_, `Heroku`_ and so on.

.. raw:: html
    <p align="center">
        <img src="docs/example.png">
    </p>

.. _AWS Lambda: https://aws.amazon.com/lambda/
.. _GCP Cloud Functions: https://cloud.google.com/functions/
.. _GCP AppEngine: https://cloud.google.com/appengine/
.. _Heroku: https://www.heroku.com/


Features
--------

DORA mainly relies on the ``dnspython`` toolkit. It can query the following
records:

- ``A``: IPv4 address;
- ``AAAA``: IPv6 address;
- ``CNAME``: Canonical name (name alias);
- ``MX``: Mail exchange (mail transfer agent name);
- ``NS``: Authoritative name server;
- ``TXT``: Text records.


Documentation
-------------

For instructions of usage, installation, deployment and overall documentation
of the code, `read the docs`_.

.. _read the docs: http://dora.rtfd.io


TODO
----

- Finish the user documentation;
- Create code documentation;
- 100% covered (*write tests*);
- Publish DORA on PyPI;
- Dockerized DORA;
- Guide: Deploying DORA on Heroku;
- Guide: Deploying DORA on AWS Lambda;
- Guide: Deploying DORA on Google App Engine;
- Guide: Deploying DORA on Google Cloud Functions;
