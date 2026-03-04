# -*- coding: utf-8 -*-
"""
Lesson 8: Pandas — Tabular Data Analysis.

Восьмой урок курса ML Zero to Hero.
Демонстрация работы с таблицами данных через библиотеку Pandas.

Author: Dmitry
Date: 2025
GitHub: https://github.com/mitjagagin/ml-zero-to-hero
"""

import json
from datetime import datetime

import pandas as pd


# =============================================================================
# ТОЧКА ВХОДА
# =============================================================================
if __name__ == "__main__":
    df: pd.DataFrame = pd.read_csv('src/data_employees.csv')
    
    print("=" * 50)
    print("АНАЛИЗ ДАННЫХ СОТРУДНИКОВ (Pandas)")
    print("=" * 50)
    print()
    
    print(f"Размер таблицы: {df.shape}")
    print(f"Столбцы: {list(df.columns)}")
    print()
    
    avg_salary: float = df['salary'].mean()
    city_salary: pd.Series = df.groupby('city')['salary'].mean()
    high_salary: pd.DataFrame = df[df['salary'] > 60000]
    churn_count: int = int(df['churn'].sum())
    churn_rate: float = churn_count / df.shape[0]
    
    report: dict[str, float] = {
        'total_employees': int(df.shape[0]),
        'avg_salary': float(avg_salary),
        'churn_count': int(churn_count),
        'churn_rate': float(churn_rate)
    }
    
    with open('src/report_employees.json', 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=4, ensure_ascii=False)
    
    print(f"Средняя зарплата: {avg_salary:.1f}")
    print(f"\nСредняя зарплата по городам:")
    print(city_salary)
    print(f"\nСотрудники с зарплатой > 60000:")
    print(high_salary[['name', 'salary', 'city']])
    print(f"\nУволилось человек: {churn_count}")
    print(f"Доля оттока: {churn_rate:.1%}")
    print("\nОтчет сохранен в report_employees.json")
    print("=" * 50)
    
    print(f"\n[INFO] Скрипт выполнен успешно в {datetime.now().strftime('%H:%M:%S')}")