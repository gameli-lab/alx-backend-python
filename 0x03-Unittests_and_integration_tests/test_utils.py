#!/usr/bin/env python3
"""
test_utils
"""
from parameterized import parameterized, parameterized_class
import unittest
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
    unit test class definition
    """
    @parameterized.expand
    def test_access_nested_map(self):
        self.assertEqual (access_nested_map({"a": {"b": {"c": 1}}}, ["a", "b", "c"]), 1)