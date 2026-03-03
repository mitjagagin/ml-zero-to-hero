# src/lesson8.py
import pandas as pd

# 1. Загрузка данных
df = pd.read_csv('src/data_employees.csv')

# 2. Просмотр данных
print("=== Первые 5 строк ===")
print(df.head())

print("\n=== Информация о данных ===")
print(f"Размер таблицы: {df.shape}")
print(f"Столбцы: {list(df.columns)}")

# TODO 1: Посчитай среднюю зарплату по всем сотрудникам
avg_salary = df["salary"].mean()  # Замени на формулу

# TODO 2: Посчитай среднюю зарплату по городам (groupby)
city_salary = df.groupby("city")["salary"].mean()  # Замени на формулу

# TODO 3: Найди сотрудников с зарплатой больше 60000
high_salary = df[df["salary"] > 60000]  # Замени на формулу

# TODO 4: Посчитай сколько человек уволилось (churn = 1)
churn_count = (df["churn"] == 1).sum()  # Замени на формулу (используй value_counts или sum)

# TODO 5: Посчитай долю оттока (churn_rate)
churn_rate = churn_count / df.shape[0]  # Замени на формулу

# TODO 6: Сохрани результат в JSON
report = {
    'total_employees': int(df.shape[0]),
    'avg_salary': float(avg_salary),
    'churn_count': int(churn_count),
    'churn_rate': float(churn_rate)
}

# Используем json для сохранения (ты уже умеешь из урока 6)
import json
with open('src/report_employees.json', 'w', encoding='utf-8') as f:
    json.dump(report, f, indent=4, ensure_ascii=False)

# Вывод результатов
print("\n=== Результаты анализа ===")
print(f"Средняя зарплата: {avg_salary}")
print(f"\nСредняя зарплата по городам:")
print(city_salary)
print(f"\nСотрудники с зарплатой > 60000:")
print(high_salary[['name', 'salary', 'city']])
print(f"\nУволилось человек: {churn_count}")
print(f"Доля оттока: {churn_rate:.2%}")
print("\nОтчет сохранен в report_employees.json")