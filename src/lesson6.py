# -*- coding: utf-8 -*-
"""
Lesson 6: Working with Files (CSV, JSON).

Шестой урок курса ML Zero to Hero.
Демонстрация загрузки данных из CSV и сохранения отчета в JSON.

Author: Dmitry
Date: 2025
GitHub: https://github.com/mitjagagin/ml-zero-to-hero
"""

import csv
import json
from datetime import datetime


# =============================================================================
# ТОЧКА ВХОДА
# =============================================================================
if __name__ == "__main__":
    # 1. Загрузка данных из CSV файла
    # CSV читает все значения как строки, даже числа
    data: list[dict[str, str]] = []
    
    with open("src/data.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    
    # 2. Подсчет статистики
    total: int = len(data)
    sum_age: float = 0
    sum_salary: float = 0
    churn_count: int = 0
    
    for row in data:  # ← ИСПРАВЛЕНО: добавлено "data"
        # Преобразование строк в числа (CSV читает всё как текст!)
        age: int = int(row["age"])
        salary: float = float(row["salary"])
        churn: int = int(row["churn"])
        
        sum_age += age
        sum_salary += salary
        churn_count += churn
    
    # Расчет средних значений
    avg_age: float = sum_age / total
    avg_salary: float = sum_salary / total
    churn_rate: float = churn_count / total
    
    # 3. Сохранение отчета в JSON
    report: dict[str, float] = {
        "total_records": total,
        "avg_age": avg_age,
        "avg_salary": avg_salary,
        "churn_rate": churn_rate
    }
    
    with open("src/report.json", "w", encoding="utf-8") as file:
        json.dump(report, file, indent=4, ensure_ascii=False)
    
    # 4. Вывод результатов
    print("Отчет сохранен в report.json")
    print(f"Средний возраст: {avg_age:.1f}")
    print(f"Средняя зарплата: {avg_salary:.1f}")
    print(f"Доля оттока: {churn_rate:.1%}")
    
    #