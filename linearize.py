#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from functools import lru_cache

class Linearizer:
    """
    Задача 8. Линеаризация вложенных списков.
    Превращает список с произвольной вложенностью в плоский список.
    """

    # ========== РЕКУРСИВНОЕ РЕШЕНИЕ (Rare) ==========
    def linearize_recursive(self, nested_list):
        """
        Рекурсивно обходит вложенный список и возвращает плоский список.
        >>> Linearizer().linearize_recursive([1, 2, [3, 4, [5, [6, []]]]])
        [1, 2, 3, 4, 5, 6]
        >>> Linearizer().linearize_recursive([])
        []
        >>> Linearizer().linearize_recursive([1, [2, [3]]])
        [1, 2, 3]
        """
        result = []
        for item in nested_list:
            if isinstance(item, list):
                result.extend(self.linearize_recursive(item))
            else:
                result.append(item)
        return result

    # ========== ИТЕРАТИВНОЕ РЕШЕНИЕ (Rare) ==========
    def linearize_iterative(self, nested_list):
        """
        Итеративно обходит вложенный список с помощью стека.
        >>> Linearizer().linearize_iterative([1, 2, [3, 4, [5, [6, []]]]])
        [1, 2, 3, 4, 5, 6]
        >>> Linearizer().linearize_iterative([])
        []
        >>> Linearizer().linearize_iterative([1, [2, [3]]])
        [1, 2, 3]
        """
        result = []
        stack = [nested_list]
        while stack:
            current = stack.pop()
            if isinstance(current, list):
                # Обходим в обратном порядке, чтобы сохранить исходный порядок
                for i in range(len(current) - 1, -1, -1):
                    stack.append(current[i])
            else:
                result.append(current)
        return result

    # ========== ОПТИМИЗИРОВАННОЕ РЕШЕНИЕ (Well-done) ==========
    @lru_cache(maxsize=128)
    def _linearize_cached(self, nested_tuple):
        """
        Вспомогательный метод с кэшированием для кортежей.
        Ускоряет повторные вызовы для одинаковых структур.
        """
        result = []
        for item in nested_tuple:
            if isinstance(item, tuple):
                result.extend(self._linearize_cached(item))
            else:
                result.append(item)
        return tuple(result)

    def linearize_optimized(self, nested_list):
        """
        Оптимизированное решение с кэшированием результатов.
        Преобразует список в кортеж для возможности хэширования.
        >>> Linearizer().linearize_optimized([1, 2, [3, 4, [5, [6, []]]]])
        [1, 2, 3, 4, 5, 6]
        >>> Linearizer().linearize_optimized([])
        []
        """
        def to_tuple(lst):
            if isinstance(lst, list):
                return tuple(to_tuple(item) for item in lst)
            return lst

        cached_result = self._linearize_cached(to_tuple(nested_list))
        return list(cached_result)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print("Все доктесты пройдены.")