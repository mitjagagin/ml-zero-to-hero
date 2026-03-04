# -*- coding: utf-8 -*-
"""
ML Metrics Library.

Библиотека функций для расчета метрик бинарной классификации.
Используется в уроках 4 и 5.

Концепции:
    TP (True Positive): Факт=1, Предсказание=1
    FP (False Positive): Факт=0, Предсказание=1
    FN (False Negative): Факт=1, Предсказание=0
    TN (True Negative): Факт=0, Предсказание=0

Author: Dmitry
Date: 2025
GitHub: https://github.com/mitjagagin/ml-zero-to-hero
"""

from typing import Any, Dict


def calculate_accuracy(y_true: list[int], y_pred: list[int]) -> float:
    """
    Вычисляет точность классификации (Accuracy).
    Формула: (Правильные предсказания) / (Все предсказания)
    """
    if len(y_true) != len(y_pred):
        raise ValueError("Длины списков должны совпадать")
    
    if len(y_true) == 0:
        return 0.0
    
    correct = 0
    for i in range(len(y_true)):
        if y_true[i] == y_pred[i]:
            correct += 1
    
    return correct / len(y_true)


def calculate_precision(y_true: list[int], y_pred: list[int]) -> float:
    """
    Вычисляет точность положительных предсказаний (Precision).
    Формула: TP / (TP + FP)
    """
    if len(y_true) != len(y_pred):
        raise ValueError("Длины списков должны совпадать")
    
    tp = 0
    fp = 0
    
    for i in range(len(y_true)):
        if y_pred[i] == 1:
            if y_true[i] == 1:
                tp += 1
            else:
                fp += 1
    
    if (tp + fp) == 0:
        return 0.0
    
    return tp / (tp + fp)


def get_model_report(
    y_true: list[int],
    y_pred: list[int],
    model_name: str = "MyModel"
) -> dict[str, float]:
    """Формирует отчет с метриками модели."""
    return {
        "model": model_name,
        "accuracy": calculate_accuracy(y_true, y_pred),
        "precision": calculate_precision(y_true, y_pred)
    }


def print_report(report: dict[str, float]) -> None:
    """Выводит отчет о метриках в консоль."""
    print("=" * 50)
    print("ОТЧЕТ ПО МЕТРИКАМ МОДЕЛИ")
    print("=" * 50)
    print(f"Model:     {report['model']}")
    print(f"Accuracy:  {report['accuracy']:.4f}")
    print(f"Precision: {report['precision']:.4f}")
    print("=" * 50)