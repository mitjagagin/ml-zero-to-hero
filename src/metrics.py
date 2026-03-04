# -*- coding: utf-8 -*-
"""
Metrics Module.

Модуль содержит функции для расчета метрик модели.
Используется в Уроке 5 для демонстрации импорта.

Author: Dmitry
Date: 2025
"""

from typing import List, Dict


def calculate_accuracy(y_true: List[int], y_pred: List[int]) -> float:
    """
    Считает долю правильных ответов (Accuracy).
    """
    correct = 0
    total = len(y_true)
    
    for i in range(total):
        if y_true[i] == y_pred[i]:
            correct += 1
    
    # Защита от деления на ноль
    if total == 0:
        return 0.0
        
    return correct / total


def calculate_precision(y_true: List[int], y_pred: List[int]) -> float:
    """
    Считает Precision (TP / (TP + FP)).
    """
    tp = 0  # True Positive
    fp = 0  # False Positive
    
    for i in range(len(y_true)):
        true = y_true[i]
        pred = y_pred[i]
        
        if pred == 1:
            if true == 1:
                tp += 1
            else:
                fp += 1
    
    # Защита от деления на ноль
    if (tp + fp) == 0:
        return 0.0
        
    return tp / (tp + fp)


def get_model_report(y_true: List[int], y_pred: List[int], model_name: str = "MyModel") -> Dict[str, float]:
    """
    Собирает отчет в словарь.
    """
    acc = calculate_accuracy(y_true, y_pred)
    prec = calculate_precision(y_true, y_pred)
    
    return {
        "model": model_name,
        "accuracy": acc,
        "precision": prec
    }