# -*- coding: utf-8 -*-
"""
Lesson 4: Functions — ML Metrics Library.

Четвертый урок курса ML Zero to Hero.
Демонстрация создания библиотеки функций для расчета метрик классификации:
Accuracy, Precision. Введение в концепции TP, FP, TN, FN.

Author: Dmitry
Date: 2025
GitHub: https://github.com/mitjagagin/ml-zero-to-hero
"""

from datetime import datetime
from typing import Dict, List


# =============================================================================
# КОНСТАНТЫ
# =============================================================================
DEFAULT_MODEL_NAME: str = "MyModel"
DECIMAL_PRECISION: int = 4


# =============================================================================
# ФУНКЦИИ
# =============================================================================
def calculate_accuracy(y_true: List[int], y_pred: List[int]) -> float:
    """
    Вычисляет точность классификации (Accuracy).

    Accuracy = (Правильные предсказания) / (Все предсказания)

    Args:
        y_true: Список фактических значений (0 или 1).
        y_pred: Список предсказанных значений (0 или 1).

    Returns:
        float: Доля правильных предсказаний (от 0 до 1).

    Raises:
        ValueError: Если длины списков не совпадают или списки пустые.
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

    Precision = TP / (TP + FP)
    
    Где:
        TP (True Positive): Факт=1, Предсказание=1
        FP (False Positive): Факт=0, Предсказание=1

    Args:
        y_true: Список фактических значений (0 или 1).
        y_pred: Список предсказанных значений (0 или 1).

    Returns:
        float: Precision (от 0 до 1). Возвращает 0.0, если не было положительных предсказаний.

    Note:
        Precision важна, когда цена ложной тревоги (FP) высока.
        Например: спам-фильтр (лучше пропустить спам, чем удалить важное письмо).
    """
    if len(y_true) != len(y_pred):
        raise ValueError("Длины списков y_true и y_pred должны совпадать")
    
    tp: int = 0  # True Positive
    fp: int = 0  # False Positive
    
    for i in range(len(y_true)):
        true: int = y_true[i]
        pred: int = y_pred[i]
        
        # Считаем только случаи, где модель предсказала 1 (Positive)
        if pred == 1:
            if true == 1:
                tp += 1  # Правильно предсказал положительный класс
            else:
                fp += 1  # Ложная тревога
    
    # Защита от деления на ноль
    if (tp + fp) == 0:
        return 0.0
    
    return tp / (tp + fp)


def get_model_report(
    y_true: List[int],
    y_pred: List[int],
    model_name: str = DEFAULT_MODEL_NAME
) -> Dict[str, float]:
    """
    Формирует отчет с метриками модели.

    Args:
        y_true: Список фактических значений (0 или 1).
        y_pred: Список предсказанных значений (0 или 1).
        model_name: Название модели для отчета.

    Returns:
        Dict[str, float]: Словарь с метриками:
            - model: название модели
            - accuracy: точность классификации
            - precision: точность положительных предсказаний
    """
    accuracy: float = calculate_accuracy(y_true, y_pred)
    precision: float = calculate_precision(y_true, y_pred)
    
    return {
        "model": model_name,
        "accuracy": accuracy,
        "precision": precision
    }


def print_report(report: Dict[str, float]) -> None:
    """
    Выводит отчет о метриках модели в консоль.

    Args:
        report: Словарь с метриками от get_model_report().
    """
    print("=" * 50)
    print("ОТЧЕТ ПО МЕТРИКАМ МОДЕЛИ")
    print("=" * 50)
    print(f"Model:     {report['model']}")
    print(f"Accuracy:  {report['accuracy']:.{DECIMAL_PRECISION}f}")
    print(f"Precision: {report['precision']:.{DECIMAL_PRECISION}f}")
    print("=" * 50)


# =============================================================================
# ТОЧКА ВХОДА
# =============================================================================
if __name__ == "__main__":
    # 1. Тестовые данные (бинарная классификация)
    # 1 = Positive (например, "болен", "спам", "отток")
    # 0 = Negative (например, "здоров", "не спам", "нет оттока")
    y_true: List[int] = [1, 0, 1, 1, 0, 1, 0, 0]
    y_pred: List[int] = [1, 0, 0, 1, 0, 1, 1, 0]
    
    print("=" * 50)
    print("БИНАРНАЯ КЛАССИФИКАЦИЯ — РАСЧЕТ МЕТРИК")
    print("=" * 50)
    print()
    
    # 2. Получение отчета
    report: Dict[str, float] = get_model_report(
        y_true,
        y_pred,
        model_name="RandomForest_v1"
    )
    
    # 3. Вывод отчета
    print_report(report)
    
    # 4. Дополнительная информация для понимания
    print("\n📊 ИНТЕРПРЕТАЦИЯ:")
    print(f"   Accuracy {report['accuracy']:.1%} — модель угадала {report['accuracy']:.1%} всех случаев")
    print(f"   Precision {report['precision']:.1%} — из всех предсказаний '1' правильных {report['precision']:.1%}")
    
    # 5. Логирование выполнения
    print(f"\n[INFO] Скрипт выполнен успешно в {datetime.now().strftime('%H:%M:%S')}")