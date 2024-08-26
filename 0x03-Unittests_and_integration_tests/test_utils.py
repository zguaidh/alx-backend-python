#!/usr/bin/env python3
"""
Unitest Module for utils script
"""


import unittest
from unittest.mock import patch, MagicMock
from parameterized import parameterized
from utils import access_nested_map
from utils import get_json
from utils import memoize
from typing import Dict, Tuple, Union, Type


class TestAccessNestedMap(unittest.TestCase):
    """ Test cases for AccessNestedMap class """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
        ])
    def test_access_nested_map(self,
                               nested_map: Dict,
                               path: Tuple,
                               expected: Union[Dict, int]) -> None:
        """ test for the method access_nested_map """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(self,
                                         nested_map: Dict,
                                         path: Tuple[str],
                                         expected: Union[Type[BaseException]]
                                         ) -> None:
        """ access nest map Exception"""
        with self.assertRaises(expected):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url: str,
                      test_payload: Dict,
                      mock_get) -> None:
        """ test that utils.get_json returns the expected result"""
        mock_response = mock_get.return_value
        mock_response.json.return_value = test_payload

        result = get_json(test_url)

        mock_get.assert_called_once_with(test_url)

        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """ TestMemoize test class """
    def test_memoize(self) -> None:
        """ Test memoize method definition"""
        class TestClass:
            """ Test Class definition"""
            def a_method(self) -> int:
                """method definition"""
                return 42

            @memoize
            def a_property(self) -> int:
                """method definition"""
                return self.a_method()

        with patch.object(
             TestClass, 'a_method', return_value=42) as mock_a_method:
            test_instance = TestClass()

            result1 = test_instance.a_property
            result2 = test_instance.a_property

            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)

            mock_a_method.assert_called_once()
