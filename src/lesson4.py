# -*- coding: utf-8 -*-
"""
Lesson 4: Functions — ML Metrics (Refactored).

Четвертый урок курса ML Zero to Hero.
Демонстрация работы с метриками классификации.

ПРИМЕЧАНИЕ: 
В целях соблюдения принципа DRY (Don't Repeat Yourself), 
функции вынесены в отдельный модуль metrics.py.
Этот файл демонстрирует использование этих функций.

Author: Dmitry
Date: 2025
GitHub: https://github.com/mitjagagin/ml-zero-to-hero
"""

from datetime import datetime
from typing import Dict

# Импортируем функции из нашего модуля metrics
from metrics import get_model_report, print_report


# =============================================================================
# ТОЧКА ВХОДА
# =============================================================================
if __name__ == "__main__":
    # 1. Тестовые данные
    y_true: list[int] = [1, 0, 1, 1, 0, 1, 0, 0]
    y_pred: list[int] = [1, 0, 0, 1, 0, 1, 1, 0]
    
    print("=" * 60)
    print("УРОК 4: БИНАРНАЯ КЛАССИФИКАЦИЯ — РАСЧЕТ МЕТРИК")
    print("=" * 60)
    print()
    
    # 2. Получение отчета (функция из metrics.py)
    report: Dict[str, float] = get_model_report(
        y_true,
        y_pred,
        model_name="RandomForest_v1"
    )
    
    # 3. Вывод отчета (функция из metrics.py)
    print_report(report)
    
    # 4. Интерпретация
    print("\n📊 ИНТЕРПРЕТАЦИЯ:")
    print(f"   Accuracy {report['accuracy']:.1%} — модель угадала {report['accuracy']:.1%} всех случаев")
    print(f"   Precision {report['precision']:.1%} — точность положительных предсказаний")
    
    # 5. Логирование
    print(f"\n[INFO] Скрипт выполнен успешно в {datetime.now().strftime('%H:%M:%S')}")