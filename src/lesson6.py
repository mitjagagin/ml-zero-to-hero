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
    # 1. Загрузка данных из CSV
    data = []
    with open("src/data.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    
    # 2. Подсчет статистики
    total = len(data)
    sum_age = 0
    sum_salary = 0
    churn_count = 0
    
    for row in data:
        # Преобразование строк в числа (CSV читает всё как текст)
        age = int(row["age"])
        salary = float(row["salary"])
        churn = int(row["churn"])
        
        sum_age += age
        sum_salary += salary
        churn_count += churn
    
    avg_age = sum_age / total
    avg_salary = sum_salary / total
    churn_rate = churn_count / total
    
    # 3. Сохранение отчета в JSON
    report = {
        "total_records": total,
        "avg_age": avg_age,
        "avg_salary": avg_salary,
        "churn_rate": churn_rate
    }
    
    with open("src/report.json", "w", encoding="utf-8") as file:
        json.dump(report, file, indent=4, ensure_ascii=False)
    
    # 4. Вывод
    print("Отчет сохранен в report.json")
    print(f"Средний возраст: {avg_age:.1f}")
    print(f"Средняя зарплата: {avg_salary:.1f}")
    print(f"Доля оттока: {churn_rate:.1%}")
    
    # 5. Логирование
    print(f"\n[INFO] Скрипт выполнен успешно в {datetime.now().strftime('%H:%M:%S')}")