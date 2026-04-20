#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest
from linearize import Linearizer

@pytest.fixture
def linearizer():
    return Linearizer()

def test_recursive_empty(linearizer):
    assert linearizer.linearize_recursive([]) == []

def test_recursive_flat(linearizer):
    assert linearizer.linearize_recursive([1, 2, 3]) == [1, 2, 3]

def test_recursive_nested(linearizer):
    assert linearizer.linearize_recursive([1, [2, [3]]]) == [1, 2, 3]

def test_recursive_example(linearizer):
    assert linearizer.linearize_recursive([1, 2, [3, 4, [5, [6, []]]]]) == [1, 2, 3, 4, 5, 6]

def test_iterative_empty(linearizer):
    assert linearizer.linearize_iterative([]) == []

def test_iterative_flat(linearizer):
    assert linearizer.linearize_iterative([1, 2, 3]) == [1, 2, 3]

def test_iterative_nested(linearizer):
    assert linearizer.linearize_iterative([1, [2, [3]]]) == [1, 2, 3]

def test_iterative_example(linearizer):
    assert linearizer.linearize_iterative([1, 2, [3, 4, [5, [6, []]]]]) == [1, 2, 3, 4, 5, 6]

def test_optimized_empty(linearizer):
    assert linearizer.linearize_optimized([]) == []

def test_optimized_flat(linearizer):
    assert linearizer.linearize_optimized([1, 2, 3]) == [1, 2, 3]

def test_optimized_nested(linearizer):
    assert linearizer.linearize_optimized([1, [2, [3]]]) == [1, 2, 3]

def test_optimized_example(linearizer):
    assert linearizer.linearize_optimized([1, 2, [3, 4, [5, [6, []]]]]) == [1, 2, 3, 4, 5, 6]

def test_all_methods_agree(linearizer):
    test_cases = [
        [],
        [1, 2, 3],
        [1, [2, [3]]],
        [1, 2, [3, 4, [5, [6, []]]]],
        [[], [[]], [[1]]],
    ]
    for case in test_cases:
        r = linearizer.linearize_recursive(case)
        i = linearizer.linearize_iterative(case)
        o = linearizer.linearize_optimized(case)
        assert r == i == o