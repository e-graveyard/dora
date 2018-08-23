D.O.R.A.
========

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


**D**\NS **O**\ver **R**\EST **A**\PI

**DORA** is a web application that provides a simple API for DNS querying
through a REST architecture. It aims to be a consumable API that's easy
to digest and easy to deploy in cloud-based solutions, such as Google App
Engine.

**DORA** mainly relies on ``dnspython`` toolkit and the ``flask`` microframework.


Requirements
------------

- Python3 (3.4 and above)
- `Flask microframework`_
- `dnspython toolkit`_

.. _Flask microframework: https://github.com/pallets/flask
.. _dnspython toolkit: https://github.com/rthalley/dnspython


Documentation
-------------

For instructions of usage, installation, deployment and overall documentation
of the code, `read the docs`_.

.. _read the docs: http://dora.rtfd.io


Similar Projects
----------------

- `dns-api.org`_ :a DNS-lookup service written in Perl.

.. _dns-api.org: https://github.com/skx/dns-api.org


TODO
----

- [ ] Finish the user documentation;
- [ ] Create code documentation;
- [ ] 100% covered (*write tests*);
- [ ] Publish DORA on PyPI;
- [ ] Dockerized DORA;
- [ ] Guide: Deploying DORA on Heroku;
- [ ] Guide: Deploying DORA on AWS Lambda;
- [ ] Guide: Deploying DORA on Google App Engine;
- [ ] Guide: Deploying DORA on Google Cloud Functions;
