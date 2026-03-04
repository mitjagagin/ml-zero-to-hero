# -*- coding: utf-8 -*-
"""
Lesson 2: Data Structures — Lists and Dictionaries.

Второй урок курса ML Zero to Hero.
Демонстрация работы со списками, словарями и базовыми операциями над ними.

Author: Dmitry
Date: 2025
GitHub: https://github.com/mitjagagin/ml-zero-to-hero
"""

from typing import Any, Dict, List


# =============================================================================
# КОНСТАНТЫ
# =============================================================================
DEFAULT_MODEL_NAME: str = "RandomForest"
DEFAULT_EPOCHS: int = 100
DEFAULT_METRICS: List[float] = [0.2, 0.1, 0.4, 0.3, 0.5]


# =============================================================================
# ФУНКЦИИ
# =============================================================================
def create_training_log(
    model_name: str = DEFAULT_MODEL_NAME,
    epochs: int = DEFAULT_EPOCHS,
    metrics: List[float] = None
) -> Dict[str, Any]:
    """
    Создает словарь с логом обучения модели.

    Args:
        model_name: Название модели (по умолчанию RandomForest).
        epochs: Количество эпох обучения.
        metrics: Список метрик точности по эпохам.

    Returns:
        Dict[str, Any]: Словарь с параметрами обучения.
    """
    if metrics is None:
        metrics = DEFAULT_METRICS.copy()
    
    return {
        "model_name": model_name,
        "epochs": epochs,
        "metrics": metrics
    }


def get_last_metric(metrics: List[float]) -> float:
    """
    Возвращает последнюю метрику из списка.

    Args:
        metrics: Список метрик точности.

    Returns:
        float: Последнее значение метрики.
    """
    return metrics[-1]


def get_best_metric(metrics: List[float]) -> float:
    """
    Возвращает лучшую (максимальную) метрику из списка.

    Args:
        metrics: Список метрик точности.

    Returns:
        float: Максимальное значение метрики.
    """
    return max(metrics)


def print_training_report(log: Dict[str, Any]) -> None:
    """
    Выводит отчет об обучении модели в консоль.

    Args:
        log: Словарь с логом обучения.
    """
    metrics: List[float] = log["metrics"]
    
    print("=" * 50)
    print("ОТЧЕТ ПО ОБУЧЕНИЮ МОДЕЛИ")
    print("=" * 50)
    print(f"Название модели: {log['model_name']}")
    print(f"Количество эпох: {log['epochs']}")
    print(f"Последняя метрика: {get_last_metric(metrics)}")
    print(f"Лучшая метрика: {get_best_metric(metrics)}")
    print("=" * 50)


def print_dict_items(data: Dict[str, Any]) -> None:
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
    # 1. Создание лога обучения
    training_log: Dict[str, Any] = create_training_log(
        model_name="model1",
        epochs=100,
        metrics=[0.2, 0.1, 0.4, 0.3, 0.5]
    )

    # 2. Вывод основного отчета
    print_training_report(training_log)

    # 3. Добавление нового ключа (статус обучения)
    training_log["is_trained"] = True

    # 4. Вывод полного содержимого словаря
    print_dict_items(training_log)

    # 5. Логирование выполнения
    from datetime import datetime
    print(f"\n[INFO] Скрипт выполнен успешно в {datetime.now().strftime('%H:%M:%S')}")