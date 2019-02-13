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


TARGET_DOMAIN = 'caian.org'


class DoraTests(unittest.TestCase):
    def resource(self, kind, domain=TARGET_DOMAIN):
        return '/{}/{}'.format(domain, kind)

    def setUp(self):
        self.app = dora.test_client()
        self.app.testing = True

    def test_root(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 404)

    def test_a_lookup(self):
        result = self.app.get(self.resource('a'))
        self.assertEqual(result.status_code, 200)

    def test_aaaa_lookup(self):
        result = self.app.get(self.resource('aaaa'))
        self.assertEqual(result.status_code, 200)

    def test_cname_lookup(self):
        result = self.app.get(self.resource('cname'))
        self.assertEqual(result.status_code, 200)

    def test_mx_lookup(self):
        result = self.app.get(self.resource('mx'))
        self.assertEqual(result.status_code, 200)

    def test_ns_lookup(self):
        result = self.app.get(self.resource('ns'))
        self.assertEqual(result.status_code, 200)

    def test_txt_lookup(self):
        result = self.app.get(self.resource('txt'))
        self.assertEqual(result.status_code, 200)

    def test_unknown_record_type(self):
        result = self.app.get(self.resource('unknown'))
        self.assertEqual(result.status_code, 400)

    def test_domain_target_not_found(self):
        result = self.app.get(self.resource('txt', 'caian.orgx'))
        self.assertEqual(result.status_code, 404)


if __name__ == '__main__':
    unittest.main()
