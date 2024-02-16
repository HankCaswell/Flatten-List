from flatten_list import flatten
import pytest

def test_flatten_simple():
    # Test a simple nested list
    nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    flattened = flatten(nested_list)
    assert flattened == [1, 2, 3, 4, 5, 6, 7, 8, 9]

def test_flatten_empty():
    # Test an empty nested list
    nested_list = []
    flattened = flatten(nested_list)
    assert flattened == []

def test_flatten_nested():
    # Test a deeply nested list
    nested_list = [1, [2, [3, 4, [5, 6]], 7], 8]
    flattened = flatten(nested_list)
    assert flattened == [1, 2, 3, 4, 5, 6, 7, 8]