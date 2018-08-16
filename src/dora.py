#!/usr/bin/env python3
# -*- coding: utf-8 -*-


__copyright__ = """
** MIT License **

Copyright (c) 2017, 2018 Caian Rais Ertl

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
__version__ = '0.1.0'
__author__ = 'Caian R. Ertl'


# Standard libraries. Should not fail.
import sys
import textwrap
from argparse import ArgumentParser
from argparse import RawTextHelpFormatter

# Required 3rd-parth libraries.
try:
    import dns.resolver
    from flask import Flask
    from flask import make_response
    from flask import render_template
    from flask_restful import Api
    from flask_restful import Resource

except ImportError as e:
    print('DORA: impossible to import 3rd-party libraries.\n'
          'Latest traceback: {0}' . format(e.args[0]))

    sys.exit(1)


class CLI:
    """Command-line interface handling class.

    This class aims to create a command-line interface to controls
    DORA's functionalities. It defines a `git`-like subcommand
    structure, where the top-level command is dora itself and each
    subcommand is a possible action (e.g. `dora start`).
    """

    def __init__(self):
        """."""
        # Top-level parser
        self.parser = ArgumentParser(
                prog=__program__,
                formatter_class=RawTextHelpFormatter,
                description=textwrap.dedent('''\
                        DORA\'s command-line interface.

                        DORA is a web application that provides a simple
                        API for DNS querying through a REST archictecture.
                        '''),
                epilog=textwrap.dedent('''\
                        This is a Free and Open-Source Software (FOSS).
                        Licensed under the MIT License.

                        Project page: <https://github.com/caianrais/dora>
                        '''))

        self.parser.add_argument(
                '-v', '--version',
                action='version',
                version='{0} ({1})'.format(
                    __program__, __version__
                ),
                help='show the application version and exit')

        self.parser.add_argument(
                '--copyright',
                action='store_true',
                dest='copyright',
                help='show the copyright information and exit')

        # Initializes the subparser
        self.sub_parser = self.parser.add_subparsers(
                dest='subcmd',
                help='DORA commands')

        # Start subcommand
        subcmd_start = self.sub_parser.add_parser(
                'start',
                help='starts DORA\'s service')

        # Start subcommand's arguments
        subcmd_start.add_argument(
                '-p', '--port',
                action='store',
                dest='port',
                type=int,
                help=textwrap.dedent('''\
                        sets the port number the application will listen to
                        default value: 80
                        '''))

        subcmd_start.add_argument(
                '-d', '--debug',
                action='store_true',
                help='enable debug mode')

    def act(self):
        argp = self.parser.parse_args()

        if argp.copyright:
            self.show_copyright()

        else:
            if argp.subcmd == 'start':
                if argp.port is None:
                    argp.port = 80
                self._start(argp.port, argp.debug)

            else:
                print('DORA: missing operand.\n'
                      'Try \'dora --help\' for more information.')

                sys.exit(1)

    def show_copyright(self):
        print(__copyright__)

    def _start(self, f_port, debug_mode):
        dora.run(debug=debug_mode,
                 host='0.0.0.0',
                 use_reloader=True,
                 port=f_port)


class Response:
    def __init__(self, question):
        self.answer = self.Answer(question)
        self.error = self.Error()

    @staticmethod
    def respond(message, code, data=None):
        response = {
            'code': code,
            'message': message,
            'status': 'success' if code < 400 else 'error'
        }

        if data:
            response['data'] = data

        return response, code

    class Answer:
        def __init__(self, question):
            self.question = question

        def respond(self, message, code, records=None):
            data = {}
            data['question'] = self.question
            if records:
                data['answer'] = {'records': records}

            return Response.respond(message, code, data)

        def success(self, records):
            return self.respond(
                'DNS lookup is successful.', 200, records
            )

        @property
        def empty_answer(self):
            return self.respond(
                'The response does not contain an answer to the question.', 204
            )

    class Error:
        @property
        def resource_not_found(self):
            return Response.respond(
                'The specified DNS resource does not exists.', 404
            )

        @property
        def target_not_found(self):
            return Response.respond(
                'The specified domain target was not found.', 404
            )

        @property
        def unknown_record_type(self):
            return Response.respond(
                'Bad Request: Unknown record type.', 400
            )


class Resolver:
    def __init__(self, domain, resource):
        self.domain = domain
        self.resource = resource

    def look(self):
        response = Response(question={
            'domain': self.domain,
            'record': self.resource
        })

        try:
            records = None
            if self.resource == 'A':
                records = self.a

            elif self.resource == 'MX':
                records = self.mx

            elif self.resource == 'NS':
                records = self.ns

            elif self.resource == 'TXT':
                records = self.txt

            else:
                return response.error.unknown_record_type

            return response.answer.success(records)

        except dns.resolver.NoAnswer:
            return response.answer.empty_answer

        except dns.resolver.NXDOMAIN:
            return response.error.target_not_found

    def query(self, resource_identifier=None):
        records = []

        query = dns.resolver.query(self.domain, self.resource)
        if resource_identifier:
            for answer in query:
                records.append({
                    resource_identifier: answer.to_text()
                })

        else:
            for answer in query:
                records.append(answer.to_text())

        return records

    @property
    def a(self):
        return self.query('ipv4')

    @property
    def ns(self):
        return self.query('nameserver')

    @property
    def txt(self):
        return self.query('text')

    @property
    def mx(self):
        records = []

        for answer in self.query():
            priority, hostname = answer.split(' ')
            records.append({
                'hostname': hostname,
                'priority': priority
            })

        return records


class DoraSplashPageHandler(Resource):
    def get(self):
        return make_response(render_template('splash.html'))


class DoraQueryRouteHandler(Resource):
    def get(self, domain, record):
        resolver = Resolver(domain, str.upper(record))
        return resolver.look()


dora = Flask(__name__)

api = Api(dora)
api.add_resource(DoraSplashPageHandler, '/')
api.add_resource(DoraQueryRouteHandler, '/<string:domain>/<string:record>')


# Needed for local execution.
if __name__ == '__main__':
    _cli = CLI()
    _cli.act()
