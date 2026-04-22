#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from functools import lru_cache

class SequenceCalculator:
    """
     Расчёт последовательности a_k, b_k.
    a_k = 2 * b_{k-1} + a_{k-1}
    b_k = 2 * a_{k-1} + b_{k-1}
    a_1 = b_1 = 1
    """

    # ========== РЕКУРСИВНОЕ РЕШЕНИЕ ==========
    def calculate_recursive(self, k):
        """
        Рекурсивно вычисляет a_k и b_k.
        >>> SequenceCalculator().calculate_recursive(1)
        (1, 1)
        >>> SequenceCalculator().calculate_recursive(2)
        (3, 3)
        >>> SequenceCalculator().calculate_recursive(3)
        (9, 9)
        """
        if k == 1:
            return 1, 1
        a_prev, b_prev = self.calculate_recursive(k - 1)
        a_k = 2 * b_prev + a_prev
        b_k = 2 * a_prev + b_prev
        return a_k, b_k

    # ========== ИТЕРАТИВНОЕ РЕШЕНИЕ ==========
    def calculate_iterative(self, k):
        """
        Итеративно вычисляет a_k и b_k.
        >>> SequenceCalculator().calculate_iterative(1)
        (1, 1)
        >>> SequenceCalculator().calculate_iterative(2)
        (3, 3)
        >>> SequenceCalculator().calculate_iterative(3)
        (9, 9)
        """
        if k == 1:
            return 1, 1
        a_prev, b_prev = 1, 1
        for _ in range(2, k + 1):
            a_curr = 2 * b_prev + a_prev
            b_curr = 2 * a_prev + b_prev
            a_prev, b_prev = a_curr, b_curr
        return a_prev, b_prev

    # ========== ОПТИМИЗИРОВАННОЕ РЕШЕНИЕ ==========
    @lru_cache(maxsize=128)
    def calculate_cached(self, k):
        """
        Вычисляет a_k и b_k с кэшированием.
        >>> SequenceCalculator().calculate_cached(1)
        (1, 1)
        >>> SequenceCalculator().calculate_cached(2)
        (3, 3)
        >>> SequenceCalculator().calculate_cached(3)
        (9, 9)
        """
        if k == 1:
            return 1, 1
        a_prev, b_prev = self.calculate_cached(k - 1)
        a_k = 2 * b_prev + a_prev
        b_k = 2 * a_prev + b_prev
        return a_k, b_k


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print("Все доктесты пройдены.")