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

    _domain = None
    _record = None
    _response = None
    _resolver = None

    def __init__(self, domain, record):
        """
        """
        self._domain = domain
        self._record = record
        self._response = []
        self._resolver = dns.resolver

    def look(self):
        """
        """
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
        mx_query = self._resolver.query(self._domain, self._record)

        for mx_data in mx_query:
            mx_item_hostname = str(mx_data.exchange)
            mx_item_priority = mx_data.preference

            self._result.append({
                'hostname': mx_item_hostname,
                'priority': mx_item_priority
                })

        return self._response

    def _dig_ns(self):
        ns_query = self._resolver.query(self._domain, self._record)
        ns_answer = ns_query.response.answer

        for ns_data in ns_answer:
            for ns_item in ns_data.items:
                self._response.append({
                    'nameserver': ns_item.to_text()
                    })

        return self._response

    def _dig_txt(self):
        txt_query = self._resolver.query(self._domain, self._record)
        txt_answer = txt_query.response.answer

        for txt_data in txt_answer:
            for txt_item in txt_data.items:
                self._response.append({
                    'text': txt_item.to_text()
                    })

        return self._response


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
