# -*- coding: utf-8 -*-
"""
ML Metrics Library.

Библиотека функций для расчета метрик бинарной классификации.
Включает: Accuracy, Precision, Recall, F1-Score.

Концепции:
    TP (True Positive): Факт=1, Предсказание=1 — правильно найден положительный класс
    FP (False Positive): Факт=0, Предсказание=1 — ложная тревога
    FN (False Negative): Факт=1, Предсказание=0 — пропуск положительного класса
    TN (True Negative): Факт=0, Предсказание=0 — правильно найден отрицательный класс

Author: Dmitry
Date: 2025
GitHub: https://github.com/mitjagagin/ml-zero-to-hero
"""

from typing import Dict, List, Tuple


# =============================================================================
# КОНСТАНТЫ
# =============================================================================
DEFAULT_MODEL_NAME: str = "MyModel"
DECIMAL_PRECISION: int = 4


# =============================================================================
# ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ
# =============================================================================
def calculate_confusion_matrix(
    y_true: List[int],
    y_pred: List[int]
) -> Tuple[int, int, int, int]:
    """
    Вычисляет элементы матрицы ошибок (Confusion Matrix).

    Args:
        y_true: Список фактических значений (0 или 1).
        y_pred: Список предсказанных значений (0 или 1).

    Returns:
        Tuple[int, int, int, int]: Кортеж (TP, FP, FN, TN).

    Raises:
        ValueError: Если длины списков не совпадают.
    """
    if len(y_true) != len(y_pred):
        raise ValueError("Длины списков y_true и y_pred должны совпадать")
    
    tp: int = 0  # True Positive
    fp: int = 0  # False Positive
    fn: int = 0  # False Negative
    tn: int = 0  # True Negative
    
    for true, pred in zip(y_true, y_pred):
        if true == 1 and pred == 1:
            tp += 1
        elif true == 0 and pred == 1:
            fp += 1
        elif true == 1 and pred == 0:
            fn += 1
        else:  # true == 0 and pred == 0
            tn += 1
    
    return tp, fp, fn, tn


# =============================================================================
# МЕТРИКИ
# =============================================================================
def calculate_accuracy(y_true: List[int], y_pred: List[int]) -> float:
    """
    Вычисляет точность классификации (Accuracy).

    Формула: Accuracy = (TP + TN) / (TP + FP + FN + TN)
           или Accuracy = (Правильные предсказания) / (Все предсказания)

    Args:
        y_true: Список фактических значений (0 или 1).
        y_pred: Список предсказанных значений (0 или 1).

    Returns:
        float: Доля правильных предсказаний (от 0 до 1).

    Raises:
        ValueError: Если списки пустые или длины не совпадают.

    Note:
        Accuracy хороша для сбалансированных классов.
        Для несбалансированных данных используйте Precision, Recall, F1.
    """
    if len(y_true) != len(y_pred):
        raise ValueError("Длины списков y_true и y_pred должны совпадать")
    
    if len(y_true) == 0:
        raise ValueError("Списки не должны быть пустыми")
    
    correct: int = 0
    total: int = len(y_true)
    
    for i in range(total):
        if y_true[i] == y_pred[i]:
            correct += 1
    
    return correct / total


def calculate_precision(y_true: List[int], y_pred: List[int]) -> float:
    """
    Вычисляет точность положительных предсказаний (Precision).

    Формула: Precision = TP / (TP + FP)

    Args:
        y_true: Список фактических значений (0 или 1).
        y_pred: Список предсказанных значений (0 или 1).

    Returns:
        float: Precision (от 0 до 1). Возвращает 0.0, если не было положительных предсказаний.

    Note:
        Precision важна, когда цена ложной тревоги (FP) высока.
        Примеры: спам-фильтр, рекомендательные системы.
    """
    if len(y_true) != len(y_pred):
        raise ValueError("Длины списков y_true и y_pred должны совпадать")
    
    tp: int = 0
    fp: int = 0
    
    for i in range(len(y_true)):
        true: int = y_true[i]
        pred: int = y_pred[i]
        
        if pred == 1:
            if true == 1:
                tp += 1
            else:
                fp += 1
    
    # Защита от деления на ноль
    if (tp + fp) == 0:
        return 0.0
    
    return tp / (tp + fp)


def calculate_recall(y_true: List[int], y_pred: List[int]) -> float:
    """
    Вычисляет полноту (Recall / Sensitivity).

    Формула: Recall = TP / (TP + FN)

    Args:
        y_true: Список фактических значений (0 или 1).
        y_pred: Список предсказанных значений (0 или 1).

    Returns:
        float: Recall (от 0 до 1). Возвращает 0.0, если не было положительных фактов.

    Note:
        Recall важна, когда цена пропуска (FN) высока.
        Примеры: медицинская диагностика, обнаружение мошенничества.
    """
    if len(y_true) != len(y_pred):
        raise ValueError("Длины списков y_true и y_pred должны совпадать")
    
    tp: int = 0
    fn: int = 0
    
    for i in range(len(y_true)):
        true: int = y_true[i]
        pred: int = y_pred[i]
        
        if true == 1:
            if pred == 1:
                tp += 1
            else:
                fn += 1
    
    # Защита от деления на ноль
    if (tp + fn) == 0:
        return 0.0
    
    return tp / (tp + fn)


def calculate_f1_score(y_true: List[int], y_pred: List[int]) -> float:
    """
    Вычисляет F1-Score (гармоническое среднее Precision и Recall).

    Формула: F1 = 2 * (Precision * Recall) / (Precision + Recall)

    Args:
        y_true: Список фактических значений (0 или 1).
        y_pred: Список предсказанных значений (0 или 1).

    Returns:
        float: F1-Score (от 0 до 1). Возвращает 0.0, если Precision + Recall = 0.

    Note:
        F1-Score полезен, когда нужен баланс между Precision и Recall.
        Используется при несбалансированных классах.
    """
    precision: float = calculate_precision(y_true, y_pred)
    recall: float = calculate_recall(y_true, y_pred)
    
    # Защита от деления на ноль
    if (precision + recall) == 0:
        return 0.0
    
    return 2 * (precision * recall) / (precision + recall)


# =============================================================================
# ОТЧЕТЫ
# =============================================================================
def get_model_report(
    y_true: List[int],
    y_pred: List[int],
    model_name: str = DEFAULT_MODEL_NAME
) -> Dict[str, float]:
    """
    Формирует полный отчет со всеми метриками модели.

    Args:
        y_true: Список фактических значений (0 или 1).
        y_pred: Список предсказанных значений (0 или 1).
        model_name: Название модели для отчета.

    Returns:
        Dict[str, float]: Словарь с метриками:
            - model: название модели
            - accuracy: точность классификации
            - precision: точность положительных предсказаний
            - recall: полнота
            - f1_score: гармоническое среднее
    """
    tp, fp, fn, tn = calculate_confusion_matrix(y_true, y_pred)
    
    return {
        "model": model_name,
        "accuracy": calculate_accuracy(y_true, y_pred),
        "precision": calculate_precision(y_true, y_pred),
        "recall": calculate_recall(y_true, y_pred),
        "f1_score": calculate_f1_score(y_true, y_pred),
        "true_positive": tp,
        "false_positive": fp,
        "false_negative": fn,
        "true_negative": tn
    }


def print_report(report: Dict[str, float]) -> None:
    """
    Выводит отчет о метриках модели в консоль.

    Args:
        report: Словарь с метриками от get_model_report().
    """
    print("=" * 60)
    print("ОТЧЕТ ПО МЕТРИКАМ МОДЕЛИ")
    print("=" * 60)
    print(f"Model:          {report['model']}")
    print("-" * 60)
    print(f"Accuracy:       {report['accuracy']:.{DECIMAL_PRECISION}f}  ({report['accuracy']:.1%})")
    print(f"Precision:      {report['precision']:.{DECIMAL_PRECISION}f}  ({report['precision']:.1%})")
    print(f"Recall:         {report['recall']:.{DECIMAL_PRECISION}f}  ({report['recall']:.1%})")
    print(f"F1-Score:       {report['f1_score']:.{DECIMAL_PRECISION}f}  ({report['f1_score']:.1%})")
    print("-" * 60)
    print("Confusion Matrix:")
    print(f"  TP: {report['true_positive']:4}  |  FP: {report['false_positive']:4}")
    print(f"  FN: {report['false_negative']:4}  |  TN: {report['true_negative']:4}")
    print("=" * 60)