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


@parameterized.expand([
        ({"a": 1}, ["a"], 1),
        ({"a": {"b": 2}}, ["a"], {"b": 2}),
        ({"a": {"b": 2}}, ["a", "b"], 2),
    ])
def test_access_nested_map(self, nested_map, path, expected):
    """
        test_access_nested_map
    """
    self.assertEqual(access_nested_map(nested_map, path), expected)


@parameterized.expand([
      ({}, ["a"]),
      ({"a": 1}, ["a", "b"])
])
def test_access_nested_map_exception(self, nested_map, path, expected):
    """
        test_access_nested_map_exception
    """
    with self.assertRaises(KeyError) as context:
        access_nested_map(nested_map, path)
    self.assertEqual(str(context.exception), f"'{expected}'")
