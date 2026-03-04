# 📘 ML Zero to Hero — Шпаргалка

Быстрая справка по всем урокам курса.

---

## 🔧 Настройка окружения

# Создать окружение
conda create -n ml_env python=3.9 -y
conda activate ml_env

# Установить библиотеки
pip install -r requirements.txt

# Git команды
git add .
git commit -m "сообщение"
git push

---

## 📝 Стандарт кода (Code Style)

### Структура файла

# -*- coding: utf-8 -*-
"""Docstring модуля."""

from datetime import datetime      # 1. Стандартные
import numpy as np                 # 2. Сторонние
from metrics import func           # 3. Локальные

# КОНСТАНТЫ
CONSTANT: int = 100

# Функции
def function() -> None:
    """Docstring функции."""
    pass

# Точка входа
if __name__ == "__main__":
    pass

---

## 🐍 Python Core

### Переменные
name: str = "Dmitry"
age: int = 25
salary: float = 50000.0
is_active: bool = True

### Списки
items: list[int] = [1, 2, 3]
items.append(4)
last = items[-1]
slice = items[1:3]
length = len(items)

### Словари
data: dict[str, float] = {"accuracy": 0.95}
value = data["accuracy"]
value = data.get("key", 0.0)
data["new_key"] = 1.0

### Условия
if score > 0.9:
    print("Отлично")
elif score > 0.7:
    print("Нормально")
else:
    print("Плохо")

### Циклы
for i in range(5):
    print(i)

for idx, val in enumerate(items):
    print(f"{idx}: {val}")

while condition:
    break
    continue

### Функции
def calculate(x: int, y: int) -> int:
    """Складывает два числа."""
    return x + y

---

## 📊 Библиотеки

### NumPy
import numpy as np
arr = np.array([1, 2, 3])
np.mean(arr)
np.std(arr)
np.max(arr)
arr[arr > 2]

### Pandas
import pandas as pd
df = pd.read_csv("data.csv")
df.head()
df.shape
df["col"].mean()
df.groupby("col")
df[df["col"] > 0]

---

## 📁 Работа с файлами

### CSV
import csv
with open("data.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["column"])

### JSON
import json
with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

---

## 🚨 Частые ошибки

| Ошибка | Решение |
|--------|---------|
| TypeError | int("5") или str(5) |
| IndexError | Проверить len() |
| KeyError | Использовать .get() |
| ModuleNotFoundError | pip install ... |
| ZeroDivisionError | Проверка на 0 |

---

## 📈 Прогресс курса

- [x] Урок 1-8: Python Core + NumPy + Pandas
- [ ] Урок 9: Scikit-learn
- [ ] Урок 10: Визуализация
- [ ] Финальный проект