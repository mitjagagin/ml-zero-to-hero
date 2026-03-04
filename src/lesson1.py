# -*- coding: utf-8 -*-
"""
Lesson 1: Python Basics & Variables.

Первый урок курса ML Zero to Hero.
Демонстрация работы с переменными, типами данных и f-strings.

Author: Dmitry
Date: 2025
GitHub: https://github.com/mitjagagin/ml-zero-to-hero
"""

from datetime import datetime


# =============================================================================
# КОНСТАНТЫ
# =============================================================================
DAYS_PER_MONTH = 30


# =============================================================================
# ФУНКЦИИ
# =============================================================================
def calculate_experience_days(months: int, days_per_month: int = DAYS_PER_MONTH) -> int:
    """Рассчитывает примерный опыт в днях на основе месяцев."""
    return months * days_per_month


def format_greeting(name: str, goal: str, days_experience: int) -> str:
    """Формирует приветственное сообщение."""
    return (
        f"{'=' * 50}\n"
        f"Привет, я {name}!\n"
        f"Моя цель: {goal}\n"
        f"Опыт в днях: ~{days_experience}\n"
        f"{'=' * 50}"
    )


# =============================================================================
# ТОЧКА ВХОДА
# =============================================================================
if __name__ == "__main__":
    # Входные данные
    user_name: str = "Dmitry"
    learning_goal: str = "Middle ML Engineer"
    months_on_vakhta: int = 12
    
    # Вычисления
    day_experience: int = calculate_experience_days(months_on_vakhta)
    
    # Вывод
    greeting: str = format_greeting(user_name, learning_goal, day_experience)
    print(greeting)
    
    # Логирование
    print(f"\n[INFO] Скрипт выполнен успешно в {datetime.now().strftime('%H:%M:%S')}")