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

from metrics import get_model_report  # Импорт из локального модуля


# =============================================================================
# ТОЧКА ВХОДА
# =============================================================================
if __name__ == "__main__":
    # Получение текущей даты и времени
    now: datetime = datetime.now()
    timestamp: str = now.strftime("%Y-%m-%d %H:%M:%S")  # Форматирование даты
    
    # Тестовые данные для классификации
    y_true: list[int] = [1, 0, 1, 1, 0, 1, 0, 0]
    y_pred: list[int] = [1, 0, 0, 1, 0, 1, 1, 0]
    
    # Получение отчета (функция из модуля metrics.py)
    report: dict[str, float] = get_model_report(
        y_true, y_pred, model_name="RandomForest_v1"
    )
    
    # Вывод отчета с временной меткой
    print("=" * 50)
    print("=== ML Model Report ===")
    print("=" * 50)
    print(f"Date:    {timestamp}")
    print(f"Model:   {report['model']}")
    print(f"Accuracy:  {report['accuracy']}")
    print(f"Precision: {report['precision']}")
    print("=" * 50)
    
    # Логирование выполнения
    print(f"\n[INFO] Отчет сгенерирован в {timestamp}")