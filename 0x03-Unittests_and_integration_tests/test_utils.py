#!/usr/bin/env python3
""" Test utils
"""
import unittest
from typing import Callable, Dict, Mapping, Sequence
from unittest.mock import MagicMock, patch
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """ Test Class access_nested_map
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_app(self, nested_map: Mapping, path: Sequence, expected: int) -> None:
        self.assertEqual(access_nested_map(nested_map, path), expected)
