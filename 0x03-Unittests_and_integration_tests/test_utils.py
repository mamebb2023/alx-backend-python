#!/usr/bin/env python3
"""
Test utils.py
"""

import unittest
from typing import Callable, Dict, Mapping, Sequence
from unittest.mock import Mock, patch
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """ Class access_nested_map function
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: Mapping, path: Sequence, expected: int) -> None:
        """ Test access_nested_map function
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a" "b"))
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping, path: Sequence) -> None:
        """ Test access_nested_map for exeptions
        """
        with self.assertRaises(KeyError) as e:
            access_nested_map(nested_map, path)
        self.assertEqual(e.exception.args[0], path[-1])


class TestGetJson(unittest.TestCase):
    """ Class for Test get_json
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch("requests.get")
    def test_get_json(self, test_url: str, test_payload: Dict[str, bool], mockGetFunc: Callable) -> None:
        """ Test get_json
        """
        test_json_mock = Mock()
        test_json_mock.json.return_value = test_payload
        mockGetFunc.return_value = test_json_mock
        main_val = get_json(test_url)
        mockGetFunc.assert_called_with(test_url)
        self.assertEqual(main_val, test_payload)


class TestMemoize(unittest.TestCase):
    """ Tests memoize decorator function
    """

    def test_memoize(self):
        """ Test memoization function
        """

        class TestClass:
            """ Class for testing purposes
            """

            def a_method(self):
                """ Test for memoization function
                """
                return 42

            @memoize
            def a_property(self):
                """ Main memoization testing function
                """
                return self.a_method()

        with patch.object(TestClass, "a_method", return_value=42) as method:
            obj = TestClass()
            self.assertEqual(obj.a_property, 42)
            self.assertEqual(obj.a_property, 42)
            method.assert_called_once()
