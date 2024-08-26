#!/usr/bin/env python3
"""
test_utils
"""
from parameterized import parameterized, parameterized_class
import unittest
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json


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


class TestGetJson(unittest.TestCase):
    """
    test get_json
    """


    @patch('utils.requests.get')
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload, mock_get):
        """
        test get_json
        """
        results = Mock()
        results.json.return_value = test_payload
        mock_get.return_value = results
        results = get_json(test_url)
        mock_get.assert_called_once_with(test_url)
        self.assertEqual(results, test_payload)