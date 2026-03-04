# -*- coding: utf-8 -*-
"""
Lesson 7: NumPy — Numerical Computing.

Седьмой урок курса ML Zero to Hero.
Демонстрация работы с массивами NumPy и векторными операциями.

Author: Dmitry
Date: 2025
GitHub: https://github.com/mitjagagin/ml-zero-to-hero
"""

import numpy as np
from datetime import datetime


# =============================================================================
# ТОЧКА ВХОДА
# =============================================================================
if __name__ == "__main__":
    # Данные
    salaries = np.array([50000, 78000, 62000, 90000, 45000, 55000, 82000, 71000])
    ages = np.array([25, 34, 29, 45, 23, 28, 38, 31])
    
    print("=" * 50)
    print("АНАЛИЗ ЗАРПЛАТ (NumPy)")
    print("=" * 50)
    
    # Расчеты
    avg_salary = np.mean(salaries)
    median_salary = np.median(salaries)
    max_salary = np.max(salaries)
    min_salary = np.min(salaries)
    std_salary = np.std(salaries)
    
    # Индекс максимальной зарплаты
    max_index = np.argmax(salaries)
    max_salary_age = ages[max_index]
    
    # Фильтрация
    high_salaries = salaries[salaries > 60000]
    
    # Вывод
    print(f"Средняя зарплата: {avg_salary:.1f}")
    print(f"Медианная зарплата: {median_salary:.1f}")
    print(f"Максимальная зарплата: {max_salary}")
    print(f"Минимальная зарплата: {min_salary}")
    print(f"Возраст самого высокооплачиваемого: {max_salary_age}")
    print(f"Зарплаты > 60000: {high_salaries}")
    print(f"Стандартное отклонение: {std_salary:.1f}")
    print("=" * 50)
    
    # Логирование
    print(f"\n[INFO] Скрипт выполнен успешно в {datetime.now().strftime('%H:%M:%S')}")