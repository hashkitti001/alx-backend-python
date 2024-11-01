#!/usr/bin/env python3
"""Tests module for the utils module."""
from typing import Dict, Tuple, Union
from unittest import TestCase
from parameterized import parameterized
from utils import (
    access_nested_map
)


class TestAccessNestedMap(TestCase):
    """Tests the access_nested_map function."""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
        self,
        nested_map: Dict,
        path: Tuple[str],
        expected: Union[Dict, int],
    ) -> None:
        """Tests the return value of the access_nested_map's output."""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_acccess_nested_map_exception(
        self,
        nested_map: Dict,
        path: Tuple[str],
        exception: Exception
    ) -> None:
        """Tests if a KeyError is raised for invalid key entries."""
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)
