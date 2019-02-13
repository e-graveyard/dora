#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Standard libraries. Should not fail.
import sys
import textwrap
from argparse import ArgumentParser
from argparse import RawTextHelpFormatter

# Required 3rd-party libraries.
try:
    import dns.resolver
    from flask import Flask
    from flask_restful import Api
    from flask_restful import Resource

except ImportError as e:
    print('DORA: impossible to import 3rd-party libraries.\n'
          'Latest traceback: {0}' . format(e.args[0]))

    sys.exit(1)


PROGRAM_NAME    = 'dora'
PROGRAM_AUTHOR  = 'Caian R. Ertl'
PROGRAM_VERSION = '0.1.0'

COPYRIGHT_INFO  = """
** MIT License **

Copyright (c) 2017, 2018, 2019 Caian R. Ertl

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


class CLI:
    """Command-line interface handling class.

    This class aims to create a command-line interface to controls
    DORA's functionalities. It defines a `git`-like subcommand
    structure, where the top-level command is dora itself and each
    subcommand is a possible action (e.g. `dora start`).
    """

    def __init__(self):
        """
        todo: documentation
        """
        self.parser = ArgumentParser(
            prog=PROGRAM_NAME,
            formatter_class=RawTextHelpFormatter,
            description=textwrap.dedent('''\
                    DORA's command-line interface.

                    DORA is a web service that provides a simple API
                    for DNS query through a REST architecture.
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
                PROGRAM_NAME, PROGRAM_VERSION
            ),
            help='show the service version and exit')

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
            help="starts DORA's service")

        # Start subcommand's arguments
        subcmd_start.add_argument(
            '-p', '--port',
            action='store',
            dest='port',
            type=int,
            help=textwrap.dedent('''\
                    sets the port number the service will listen to
                    default value: 80
                    '''))

        subcmd_start.add_argument(
            '-d', '--debug',
            action='store_true',
            help='enable debug mode')

    def act(self):
        """
        todo: documentation
        """
        argp = self.parser.parse_args()

        if argp.copyright:
            print(COPYRIGHT_INFO)
            return

        if argp.subcmd == 'start':
            dora.run(debug=argp.debug,
                     host='0.0.0.0',
                     use_reloader=True,
                     port=argp.port or 80)

        else:
            print("DORA: missing operand.\n"
                  "Try 'dora --help' for more information.")

            sys.exit(1)


class Response:
    """
    todo: documentation
    """
    def __init__(self, question):
        """
        todo: documentation
        """
        self.answer = self.Answer(question)
        self.error = self.Error()

    @staticmethod
    def respond(message, code, data=None):
        """
        todo: documentation
        """
        response = {
            'code': code,
            'message': message,
            'status': 'success' if code < 400 else 'error'
        }

        if data:
            response['data'] = data

        return response, code

    class Answer:
        """
        todo: documentation
        """
        def __init__(self, question):
            """
            todo: documentation
            """
            self.question = question

        def respond(self, message, code, records=None):
            """
            todo: documentation
            """
            data = {}
            data['question'] = self.question
            if records:
                data['answer'] = {'records': records}

            return Response.respond(message, code, data)

        def success(self, records):
            """
            todo: documentation
            """
            return self.respond(
                'DNS lookup successfully made.', 200, records
            )

        @property
        def empty_answer(self):
            """
            todo: documentation
            """
            return self.respond(
                'The response does not contain an answer to the question.', 200
            )

    class Error:
        """
        todo: documentation
        """
        @property
        def target_not_found(self):
            """
            todo: documentation
            """
            return Response.respond(
                'The specified domain target was not found.', 404
            )

        @property
        def unknown_record_type(self):
            """
            todo: documentation
            """
            return Response.respond(
                'Bad Request: Unknown record type.', 400
            )


class Resolver:
    """
    todo: documentation
    """
    def __init__(self, domain, record):
        """
        todo: documentation
        """
        self.domain = domain
        self.record = record
        self.dns_resources = {
            'A'    : self.a,
            'AAAA' : self.aaaa,
            'CNAME': self.cname,
            'MX'   : self.mx,
            'NS'   : self.ns,
            'TXT'  : self.txt
        }

    @property
    def available_resources(self):
        """
        todo: documentation
        """
        for key, _ in self.dns_resources.items():
            yield key

    def look(self):
        """
        todo: documentation
        """
        response = Response(question={
            'domain': self.domain,
            'record': self.record
        })

        try:
            if self.record not in self.available_resources:
                return response.error.unknown_record_type

            return response.answer.success(
                [res for res in self.dns_resources[self.record]()]
            )

        except dns.resolver.NoAnswer:
            return response.answer.empty_answer

        except dns.resolver.NXDOMAIN:
            return response.error.target_not_found

    def query(self, resource_identifier=None):
        """
        todo: documentation
        """
        query = dns.resolver.query(self.domain, self.record)

        if resource_identifier:
            for answer in query:
                yield {resource_identifier: answer.to_text()}

        else:
            for answer in query:
                yield answer.to_text()

    def a(self):
        """
        todo: documentation
        """
        return self.query('ipv4')

    def aaaa(self):
        """
        todo: documentation
        """
        return self.query('ipv6')

    def cname(self):
        """
        todo: documentation
        """
        return self.query('canonical')

    def ns(self):
        """
        todo: documentation
        """
        return self.query('nameserver')

    def txt(self):
        """
        todo: documentation
        """
        return self.query('text')

    def mx(self):
        """
        todo: documentation
        """
        for answer in self.query():
            priority, hostname = answer.split(' ')
            yield {'hostname': hostname, 'priority': priority}


class DoraQueryRouteHandler(Resource):
    """
    todo: documentation
    """
    def get(self, domain, record):
        """
        todo: documentation
        """
        resolver = Resolver(domain, str.upper(record))
        return resolver.look()


dora = Flask(__name__)

api = Api(dora)
api.add_resource(DoraQueryRouteHandler, '/<string:domain>/<string:record>')


# Needed for local execution.
if __name__ == '__main__':
    cli = CLI()
    cli.act()
