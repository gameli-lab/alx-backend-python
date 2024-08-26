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
        self.assertEqual(access_nested_map({"a": {"b": 1}},
                                           ["a", "b"]), 1)


@parameterized.expand
def test_access_nested_map_exception(self):
        with self.assertRaises(KeyError):
            access_nested_map({}, ["a",])
            access_nested_map({"a": 1}, ["a", "b"])
