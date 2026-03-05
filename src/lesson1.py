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
DAYS_PER_MONTH = 30  # Среднее количество дней в месяце для расчётов


# =============================================================================
# ФУНКЦИИ
# =============================================================================
def calculate_experience_days(months: int, days_per_month: int = DAYS_PER_MONTH) -> int:
    """
    Рассчитывает примерный опыт в днях на основе месяцев.
    
    Args:
        months: Количество месяцев опыта.
        days_per_month: Дней в месяце (по умолчанию 30).
    
    Returns:
        int: Примерное количество дней опыта.
    """
    return months * days_per_month


def format_greeting(name: str, goal: str, days_experience: int) -> str:
    """
    Формирует приветственное сообщение.
    
    Args:
        name: Имя пользователя.
        goal: Цель обучения.
        days_experience: Опыт в днях.
    
    Returns:
        str: Отформатированное приветствие.
    """
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
    # Входные данные о пользователе
    user_name: str = "Dmitry"
    learning_goal: str = "Middle ML Engineer"
    months_on_vakhta: int = 12  # Опыт работы вахтовым методом
    
    # Расчёт опыта в днях
    day_experience: int = calculate_experience_days(months_on_vakhta)
    
    # Формирование и вывод приветствия
    greeting: str = format_greeting(user_name, learning_goal, day_experience)
    print(greeting)
    
    # Логирование времени выполнения
    print(f"\n[INFO] Скрипт выполнен успешно в {datetime.now().strftime('%H:%M:%S')}")