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
# Responder
#------------------------------
class Responder:
    """."""

    _code = None
    _message = None
    _status = None

    def make_response(self):
        """."""
        message = {
                'code': self._code,
                'message': self._message,
                'status': self._status
            }

        return message

    @property
    def resource_not_found(self):
        """."""

        return self.make_response()

    @property
    def target_not_found(self):
        """."""
        self._code = 404
        self._message = 'The specified domain target was not found.'
        self._status = 'error'

        return self.make_response()

    @property
    def unknown_record_type(self):
        """."""
        self._code = 400
        self._message = 'Bad Request: Unknown record type.'
        self._status = 'error'

        return self.make_response()

    @property
    def empty_answer(self):
        """."""
        self._code = 204
        self._message = 'The response does not contain an answer to the question.'
        self._status = 'success'

        return self.make_response()

    @property
    def success(self):
        """."""
        self._code = 200
        self._message = 'DNS lookup is successful.'
        self._status = 'success'

        return self.make_response()



#------------------------------
# ResolverException
#------------------------------
class ResolverException(Exception):
    """Base exception class for Resolver exceptions"""


class TargetNotFound(ResolverException):
    """."""


class UnknownRecordType(ResolverException):
    """."""


class EmptyAnswer(ResolverException):
    """."""


#------------------------------
# Resolver
#------------------------------
class Resolver:
    """."""

    _domain = None
    _record = None
    _answer = None
    _resolver = None

    def __init__(self, domain, record):
        """."""
        self._domain = domain
        self._record = record
        self._answer = []
        self._resolver = dns.resolver

    def look(self):
        """."""
        try:
            if self._record == 'A':
                return self._dig_a()

            elif self._record == 'MX':
                return self._dig_mx()

            elif self._record == 'NS':
                return self._dig_ns()

            elif self._record == 'TXT':
                return self._dig_txt()

            else:
                raise dns.rdatatype.UnknownRdatatype

        except dns.resolver.NXDOMAIN:
            raise TargetNotFound

        except dns.resolver.NoAnswer:
            raise EmptyAnswer

        except dns.rdatatype.UnknownRdatatype:
            raise UnknownRecordType

    def _dig_a(self):
        """."""
        pass

    def _dig_mx(self):
        """."""
        mx_query = self._resolver.query(self._domain, self._record)

        for mx_data in mx_query:
            mx_item_hostname = str(mx_data.exchange)
            mx_item_priority = mx_data.preference

            self._answer.append({
                'hostname': mx_item_hostname,
                'priority': mx_item_priority
                })

        return self._answer

    def _dig_ns(self):
        """."""
        ns_query = self._resolver.query(self._domain, self._record)
        ns_answer = ns_query.response.answer

        for ns_data in ns_answer:
            for ns_item in ns_data.items:
                self._answer.append({
                    'nameserver': ns_item.to_text()
                    })

        return self._answer

    def _dig_txt(self):
        """."""
        txt_query = self._resolver.query(self._domain, self._record)
        txt_answer = txt_query.response.answer

        for txt_data in txt_answer:
            for txt_item in txt_data.items:
                self._answer.append({
                    'text': txt_item.to_text()
                    })

        return self._answer


# ------------------------------

responder = Responder()
application = Flask(__name__)


@application.route('/')
def display_splash():
    """."""
    return render_template('splash.html')


@application.route('/dora/v1.0/<string:record_type>/<string:domain>')
def perform_lookup(record_type, domain):
    """."""
    record_type = str.upper(record_type)

    resolver = Resolver(domain, record_type)

    try:
        answer = {'records': resolver.look()}
        response = responder.success

    except TargetNotFound:
        answer = None
        response = responder.target_not_found

    except UnknownRecordType:
        answer = None
        response = responder.unknown_record_type

    except EmptyAnswer:
        answer = None
        response = responder.empty_answer

    message = {
            'code': response['code'],
            'data': {
                'answer': answer,
                'question': {
                        'target': domain,
                        'record': record_type
                    }
                },
            'message': response['message'],
            'status': response['status']

            }

    return jsonify(message)


@application.errorhandler(404)
def not_found():
    """."""
    pass


@application.errorhandler(500)
def internal_error():
    """."""
    pass


if __name__ == '__main__':
    # Needed for local execution.
    application.run(debug        = True,
                    host         = '0.0.0.0',
                    use_reloader = True,
                    port         = 8080)

