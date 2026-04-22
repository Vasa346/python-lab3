#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest
from linearize import Linearizer
from task2 import SequenceCalculator


@pytest.fixture
def linearizer():
    return Linearizer()


@pytest.fixture
def calculator():
    return SequenceCalculator()


def test_recursive_empty(linearizer):
    assert linearizer.linearize_recursive([]) == []


def test_recursive_flat(linearizer):
    assert linearizer.linearize_recursive([1, 2, 3]) == [1, 2, 3]


def test_recursive_nested(linearizer):
    assert linearizer.linearize_recursive([1, [2, [3]]]) == [1, 2, 3]


def test_recursive_example(linearizer):
    assert linearizer.linearize_recursive([1, 2, [3, 4, [5, [6, []]]]]) == [
        1,
        2,
        3,
        4,
        5,
        6,
    ]


def test_iterative_empty(linearizer):
    assert linearizer.linearize_iterative([]) == []


def test_iterative_flat(linearizer):
    assert linearizer.linearize_iterative([1, 2, 3]) == [1, 2, 3]


def test_iterative_nested(linearizer):
    assert linearizer.linearize_iterative([1, [2, [3]]]) == [1, 2, 3]


def test_iterative_example(linearizer):
    assert linearizer.linearize_iterative([1, 2, [3, 4, [5, [6, []]]]]) == [
        1,
        2,
        3,
        4,
        5,
        6,
    ]


def test_optimized_empty(linearizer):
    assert linearizer.linearize_optimized([]) == []


def test_optimized_flat(linearizer):
    assert linearizer.linearize_optimized([1, 2, 3]) == [1, 2, 3]


def test_optimized_nested(linearizer):
    assert linearizer.linearize_optimized([1, [2, [3]]]) == [1, 2, 3]


def test_optimized_example(linearizer):
    assert linearizer.linearize_optimized([1, 2, [3, 4, [5, [6, []]]]]) == [
        1,
        2,
        3,
        4,
        5,
        6,
    ]


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


def test_sequence_recursive(calculator):
    assert calculator.calculate_recursive(1) == (1, 1)
    assert calculator.calculate_recursive(2) == (3, 3)
    assert calculator.calculate_recursive(3) == (9, 9)


def test_sequence_iterative(calculator):
    assert calculator.calculate_iterative(1) == (1, 1)
    assert calculator.calculate_iterative(2) == (3, 3)
    assert calculator.calculate_iterative(3) == (9, 9)


def test_sequence_cached(calculator):
    assert calculator.calculate_cached(1) == (1, 1)
    assert calculator.calculate_cached(2) == (3, 3)
    assert calculator.calculate_cached(3) == (9, 9)


def test_sequence_all_methods_agree(calculator):
    for k in range(1, 10):
        r = calculator.calculate_recursive(k)
        i = calculator.calculate_iterative(k)
        c = calculator.calculate_cached(k)
        assert r == i == c
