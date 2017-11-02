# -*- coding: utf-8 -*-

"""
** MIT License **

Copyright (c) 2017 Caian Rais Ertl

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


__program__ = 'dora'
__version__ = 'alpha-0.1'
__author__  = 'Caian R. Ertl'


import sys
import logging

try:
    from flask import Flask
    from flask import render_template
    from flask import jsonify
    import dns.resolver
except ImportError:
    sys.exit(1)


#------------------------------
# Response
#------------------------------
class Response:

    def __init__(self):
        pass


#------------------------------
# ResolverException
#------------------------------
class ResolverException:

    def __init__(self):
        pass


#------------------------------
# Resolver
#------------------------------
class Resolver:
    """
    """

    def __init__(self, domain, record):
        """
        """
        self._domain = domain
        self._record = record
        self._result = []
        self._resolver = dns.resolver

    def look(self):
        if self._domain == None or self._record == None:
            pass

        elif self._record == 'A':
            self._dig_a

        elif self._record == 'MX':
            self._dig_mx

        elif self._record == 'NS':
            self._dig_ns

        elif self._record == 'TXT':
            self._dig_txt

        else:
            pass

    def _dig_a(self):
        pass

    def _dig_mx(self):
        pass

    def _dig_ns(self):
        pass

    def _dig_txt(self):
        pass


application = Flask(__name__)


@application.route('/')
def display_splash():
     return render_template('splash.html')


if __name__ == '__main__':
    # Needed for local execution.
    application.run(debug        = True,
                    host         = '0.0.0.0',
                    use_reloader = False,
                    port         = 8080)
