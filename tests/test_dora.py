#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import unittest
from os.path import dirname
from os.path import abspath

sys.path.append(
    '{0}/dora'.format(dirname(dirname(abspath(__file__))))
)

from dora import dora
from dora import CLI


TARGET_DOMAIN = 'caian.org'


class DoraServiceTests(unittest.TestCase):
    """
    todo: documentation
    """

    def setUp(self):
        """
        todo: documentation
        """
        self.app = dora.test_client()
        self.app.testing = True

    def resource(self, kind, domain=TARGET_DOMAIN):
        """
        todo: documentation
        """
        return '/{}/{}'.format(domain, kind)

    def test_root(self):
        """
        todo: documentation
        """
        result = self.app.get('/')
        self.assertEqual(result.status_code, 404)

    def test_a_lookup(self):
        """
        todo: documentation
        """
        result = self.app.get(self.resource('a'))
        self.assertEqual(result.status_code, 200)

    def test_aaaa_lookup(self):
        """
        todo: documentation
        """
        result = self.app.get(self.resource('aaaa'))
        self.assertEqual(result.status_code, 200)

    def test_cname_lookup(self):
        """
        todo: documentation
        """
        result = self.app.get(self.resource('cname'))
        self.assertEqual(result.status_code, 200)

    def test_mx_lookup(self):
        """
        todo: documentation
        """
        result = self.app.get(self.resource('mx'))
        self.assertEqual(result.status_code, 200)

    def test_ns_lookup(self):
        """
        todo: documentation
        """
        result = self.app.get(self.resource('ns'))
        self.assertEqual(result.status_code, 200)

    def test_txt_lookup(self):
        """
        todo: documentation
        """
        result = self.app.get(self.resource('txt'))
        self.assertEqual(result.status_code, 200)

    def test_unknown_record_type(self):
        """
        todo: documentation
        """
        result = self.app.get(self.resource('unknown'))
        self.assertEqual(result.status_code, 400)

    def test_domain_target_not_found(self):
        """
        todo: documentation
        """
        result = self.app.get(self.resource('txt', 'caian.orgx'))
        self.assertEqual(result.status_code, 404)


class DoraCLITests(unittest.TestCase):
    """
    todo: documentation
    """

    def setUp(self):
        """
        todo: documentation
        """
        self.cli = CLI()

    def test_empty_args(self):
        """
        todo: documentation
        """
        return_code = self.cli.act([])
        self.assertEqual(return_code, 1)


if __name__ == '__main__':
    unittest.main()
