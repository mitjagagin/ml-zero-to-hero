# -*- coding: utf-8 -*-
"""
Lesson 4: Functions — ML Metrics.

Четвертый урок курса ML Zero to Hero.
Демонстрация использования библиотеки метрик из metrics.py.

Author: Dmitry
Date: 2025
GitHub: https://github.com/mitjagagin/ml-zero-to-hero
"""

from datetime import datetime

from metrics import get_model_report, print_report


# =============================================================================
# ТОЧКА ВХОДА
# =============================================================================
if __name__ == "__main__":
    # Тестовые данные для бинарной классификации
    # 1 = Positive (например, "отток", "спам", "болен")
    # 0 = Negative (например, "нет оттока", "не спам", "здоров")
    y_true: list[int] = [1, 0, 1, 1, 0, 1, 0, 0]  # Фактические значения
    y_pred: list[int] = [1, 0, 0, 1, 0, 1, 1, 0]  # Предсказания модели
    
    print("=" * 50)
    print("БИНАРНАЯ КЛАССИФИКАЦИЯ — РАСЧЕТ МЕТРИК")
    print("=" * 50)
    print()
    
    # Получение отчета из модуля metrics.py
    report: dict[str, float] = get_model_report(
        y_true, y_pred, model_name="RandomForest_v1"
    )
    
    # Вывод отчета (функция из metrics.py)
    print_report(report)
    
    # Интерпретация метрик для понимания
    print("\n📊 ИНТЕРПРЕТАЦИЯ:")
    print(f"   Accuracy {report['accuracy']:.1%} — доля правильных предсказаний")
    print(f"   Precision {report['precision']:.1%} — точность положительных")
    
    # Логирование выполнения
    print(f"\n[INFO] Скрипт выполнен успешно в {datetime.now().strftime('%H:%M:%S')}")