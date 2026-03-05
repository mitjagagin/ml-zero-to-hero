# -*- coding: utf-8 -*-
"""
Lesson 7: NumPy — Numerical Computing.

Седьмой урок курса ML Zero to Hero.
Демонстрация работы с массивами NumPy и векторными операциями.

Author: Dmitry
Date: 2025
GitHub: https://github.com/mitjagagin/ml-zero-to-hero
"""

from datetime import datetime

import numpy as np


# =============================================================================
# ТОЧКА ВХОДА
# =============================================================================
if __name__ == "__main__":
    # Создание массивов NumPy (быстрее списков Python)
    salaries: np.ndarray = np.array([50000, 78000, 62000, 90000, 45000, 55000, 82000, 71000])
    ages: np.ndarray = np.array([25, 34, 29, 45, 23, 28, 38, 31])
    
    print("=" * 50)
    print("АНАЛИЗ ЗАРПЛАТ (NumPy)")
    print("=" * 50)
    
    # Векторные операции (без циклов!)
    avg_salary: float = np.mean(salaries)      # Среднее значение
    median_salary: float = np.median(salaries) # Медиана
    max_salary: float = np.max(salaries)       # Максимум
    min_salary: float = np.min(salaries)       # Минимум
    std_salary: float = np.std(salaries)       # Стандартное отклонение
    
    # Поиск индекса максимальной зарплаты
    max_index: int = int(np.argmax(salaries))  # Индекс максимума
    max_salary_age: int = int(ages[max_index]) # Возраст по индексу
    
    # Фильтрация массива (векторная операция)
    high_salaries: np.ndarray = salaries[salaries > 60000]
    
    # Вывод результатов
    print(f"Средняя зарплата: {avg_salary:.1f}")
    print(f"Медианная зарплата: {median_salary:.1f}")
    print(f"Максимальная зарплата: {max_salary}")
    print(f"Минимальная зарплата: {min_salary}")
    print(f"Возраст самого высокооплачиваемого: {max_salary_age}")
    print(f"Зарплаты > 60000: {high_salaries}")
    print(f"Стандартное отклонение: {std_salary:.1f}")
    print("=" * 50)
    
    # Логирование выполнения
    print(f"\n[INFO] Скрипт выполнен успешно в {datetime.now().strftime('%H:%M:%S')}")