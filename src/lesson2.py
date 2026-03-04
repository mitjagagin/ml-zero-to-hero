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
from typing import Any, Dict, List


# =============================================================================
# КОНСТАНТЫ
# =============================================================================
DEFAULT_MODEL_NAME: str = "RandomForest"
DEFAULT_METRICS: List[float] = [0.2, 0.1, 0.4, 0.3, 0.5]


# =============================================================================
# ФУНКЦИИ
# =============================================================================
def create_training_log(
    model_name: str = DEFAULT_MODEL_NAME,
    metrics: List[float] = None
) -> Dict[str, Any]:
    """Создает словарь с логом обучения модели."""
    if metrics is None:
        metrics = DEFAULT_METRICS.copy()
    
    return {
        "model_name": model_name,
        "metrics": metrics
    }


def print_training_report(log: Dict[str, Any]) -> None:
    """Выводит отчет об обучении модели в консоль."""
    metrics: List[float] = log["metrics"]
    
    print("=" * 50)
    print("ОТЧЕТ ПО ОБУЧЕНИЮ МОДЕЛИ")
    print("=" * 50)
    print(f"Название модели: {log['model_name']}")
    print(f"Последняя метрика: {metrics[-1]}")
    print(f"Лучшая метрика: {max(metrics)}")
    print("=" * 50)


def print_dict_items(data: Dict[str, Any]) -> None:
    """Выводит содержимое словаря построчно."""
    print("\nСодержимое словаря:")
    print("-" * 50)
    for key, value in data.items():
        print(f"{key} -> {value}")
    print("-" * 50)


# =============================================================================
# ТОЧКА ВХОДА
# =============================================================================
if __name__ == "__main__":
    # Создание лога
    training_log: Dict[str, Any] = create_training_log(
        model_name="model1",
        metrics=[0.2, 0.1, 0.4, 0.3, 0.5]
    )
    
    # Вывод отчета
    print_training_report(training_log)
    
    # Добавление статуса
    training_log["is_trained"] = True
    
    # Вывод словаря
    print_dict_items(training_log)
    
    # Логирование
    print(f"\n[INFO] Скрипт выполнен успешно в {datetime.now().strftime('%H:%M:%S')}")