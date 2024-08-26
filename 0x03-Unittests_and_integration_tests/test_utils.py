#!/usr/bin/env python3
"""
unit test module for utils.access_nested_map.
"""
import unittest
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """
    Test Cases for the access_nested_map
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ], names=["nested_map", "path", "expected"])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        Test method to test the access_nested_map
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)


if __name__ == '__main__':
    unittest.main()
