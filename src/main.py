# -*- coding: utf-8 -*-
"""
Lesson 5: Modules and Import.

Пятый урок курса ML Zero to Hero.
Демонстрация разделения кода на модули и импорта функций.

Author: Dmitry
Date: 2025
GitHub: https://github.com/mitjagagin/ml-zero-to-hero
"""

from datetime import datetime
from typing import Dict

from metrics import get_model_report


# =============================================================================
# ТОЧКА ВХОДА
# =============================================================================
if __name__ == "__main__":
    # Дата и время
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
    
    # Данные
    y_true = [1, 0, 1, 1, 0, 1, 0, 0]
    y_pred = [1, 0, 0, 1, 0, 1, 1, 0]
    
    # Отчет
    report: Dict[str, float] = get_model_report(
        y_true, y_pred, model_name="RandomForest_v1"
    )
    
    # Вывод
    print("=" * 50)
    print("=== ML Model Report ===")
    print("=" * 50)
    print(f"Date:    {timestamp}")
    print(f"Model:   {report['model']}")
    print(f"Accuracy:  {report['accuracy']}")
    print(f"Precision: {report['precision']}")
    print("=" * 50)
    
    # Логирование
    print(f"\n[INFO] Отчет сгенерирован в {timestamp}")