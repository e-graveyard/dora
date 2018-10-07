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


class DoraTests(unittest.TestCase):
    def setUp(self):
        self.app = dora.test_client()
        self.app.testing = True

    def test_home_page(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)


if __name__ == '__main__':
    unittest.main()
