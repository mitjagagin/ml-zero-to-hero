# -*- coding: utf-8 -*-
"""
Lesson 2: Data Structures — Lists and Dictionaries.

Второй урок курса ML Zero to Hero.
Демонстрация работы со списками, словарями и базовыми операциями.

Author: Dmitry
Date: 2025
GitHub: https://github.com/mitjagagin/ml-zero-to-hero
"""

from datetime import datetime
from typing import Any


# =============================================================================
# КОНСТАНТЫ
# =============================================================================
DEFAULT_MODEL_NAME: str = "RandomForest"
DEFAULT_METRICS: list[float] = [0.2, 0.1, 0.4, 0.3, 0.5]


# =============================================================================
# ФУНКЦИИ
# =============================================================================
def create_training_log(
    model_name: str = DEFAULT_MODEL_NAME,
    metrics: list[float] = None
) -> dict[str, Any]:
    """
    Создает словарь с логом обучения модели.
    
    Args:
        model_name: Название модели.
        metrics: Список метрик точности.
    
    Returns:
        dict[str, Any]: Словарь с параметрами обучения.
    """
    if metrics is None:
        metrics = DEFAULT_METRICS.copy()  # Копируем чтобы не менять оригинал
    
    return {
        "model_name": model_name,
        "metrics": metrics
    }


def print_training_report(log: dict[str, Any]) -> None:
    """
    Выводит отчет об обучении модели в консоль.
    
    Args:
        log: Словарь с логом обучения.
    """
    metrics: list[float] = log["metrics"]
    
    print("=" * 50)
    print("ОТЧЕТ ПО ОБУЧЕНИЮ МОДЕЛИ")
    print("=" * 50)
    print(f"Название модели: {log['model_name']}")
    print(f"Последняя метрика: {metrics[-1]}")  # [-1] — последний элемент
    print(f"Лучшая метрика: {max(metrics)}")    # max() — максимальное значение
    print("=" * 50)


def print_dict_items(data: dict[str, Any]) -> None:
    """
    Выводит содержимое словаря построчно.
    
    Args:
        data: Словарь для вывода.
    """
    print("\nСодержимое словаря:")
    print("-" * 50)
    for key, value in data.items():
        print(f"{key} -> {value}")
    print("-" * 50)


# =============================================================================
# ТОЧКА ВХОДА
# =============================================================================
if __name__ == "__main__":
    # Создание лога обучения
    training_log: dict[str, Any] = create_training_log(
        model_name="model1",
        metrics=[0.2, 0.1, 0.4, 0.3, 0.5]
    )
    
    # Вывод основного отчета
    print_training_report(training_log)
    
    # Добавление нового ключа (статус обучения)
    training_log["is_trained"] = True
    
    # Вывод полного содержимого словаря
    print_dict_items(training_log)
    
    # Логирование выполнения
    print(f"\n[INFO] Скрипт выполнен успешно в {datetime.now().strftime('%H:%M:%S')}")