# Лабораторная работа №3. Рекурсия

## Вариант 8

## Условия задач

### Задача 1
Функция для линеаризации вложенных списков. Превратить список с произвольной вложенностью в плоский список.

### Задача 2
Функция для расчёта последовательности:
a_k = 2 * b_{k-1} + a_{k-1}
b_k = 2 * a_{k-1} + b_{k-1}
a_1 = b_1 = 1


## Описание проделанной работы
- Создан репозиторий `python-lab3` на GitHub.
- Склонирован в `D:\Xlam\python\python-lab3`.
- Создан файл `linearize.py` с классом `Linearizer` и тремя методами:
  - `linearize_recursive` – рекурсивное решение.
  - `linearize_iterative` – итеративное решение без рекурсии.
  - `linearize_optimized` – оптимизированное решение с кэшированием.
- Создан файл `task2.py` с классом `SequenceCalculator` и тремя методами:
  - `calculate_recursive` – рекурсивное решение.
  - `calculate_iterative` – итеративное решение.
  - `calculate_cached` – оптимизированное решение с кэшированием.
- Добавлены доктесты в оба файла.
- Создан файл `test_tasks.py` с тестами `pytest` для обеих задач.
- Проверены доктесты – 17 passed.
- Проверены тесты `pytest` – 17 passed.
- Загружены все файлы на GitHub.

## Скриншоты результатов

1. Запуск linearize.py (линеаризация списка)
<img width="920" height="81" alt="изображение" src="https://github.com/user-attachments/assets/79b15e31-b670-4011-a3e7-4cb65f1c7e54" />

2. Запуск task2.py (расчёт последовательности)
<img width="929" height="118" alt="изображение" src="https://github.com/user-attachments/assets/39518569-ae09-41ec-a5e5-1a48fdacaedf" />


## Ссылки на используемые материалы
- [Официальная документация Python](https://docs.python.org/3/)
- [Документация pytest](https://docs.pytest.org/)
- [Модуль functools.lru_cache](https://docs.python.org/3/library/functools.html)
