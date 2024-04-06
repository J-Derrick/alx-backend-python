#!/usr/bin/env python3
"""
Parametize a unit test
"""
import unitest
from parameterized import parameterized
from utils import access_nested_map

class TestAccessNestedMap(unittest.TestCase)
    """
    class that inherits from unittest.TestCase
    """
    @parameterized.expand([
        nested_map={"a": 1}, path=("a",)
        nested_map={"a": {"b": 2}}, path=("a",)
        nested_map={"a": {"b": 2}}, path=("a", "b")
        ])
       def test_access_nested_map(self, nested_map, path, expected):
        """
        method to test that the method returns what it is supposed to.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

if __name__=='__main__':
    unitest.main()
