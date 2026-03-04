# -*- coding: utf-8 -*-
"""
Lesson 5: Modules and Import.

Пятый урок курса ML Zero to Hero.
Демонстрация разделения кода на модули и импорта функций.

Этот файл (main.py) импортирует функции из файла metrics.py.
Это показывает, как строить структуру проекта из нескольких файлов.

Author: Dmitry
Date: 2025
GitHub: https://github.com/mitjagagin/ml-zero-to-hero
"""

# =============================================================================
# ИМПОРТЫ
# =============================================================================

# Импортируем стандартный модуль для работы с датой
from datetime import datetime

# Импортируем свои функции из локального модуля metrics.py
# Файл metrics.py должен лежать в той же папке (src)
from metrics import get_model_report


# =============================================================================
# ТОЧКА ВХОДА
# =============================================================================
if __name__ == "__main__":
    # 1. Получаем текущую дату и время
    # datetime.now() возвращает объект с текущей датой
    # strftime форматирует его в строку (например, "2025-02-15 14:30:00")
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
    
    # 2. Данные для теста (списки)
    y_true = [1, 0, 1, 1, 0, 1, 0, 0]
    y_pred = [1, 0, 0, 1, 0, 1, 1, 0]
    
    # 3. Получаем отчет
    # Вызываем функцию из модуля metrics.py
    report = get_model_report(y_true, y_pred, model_name="RandomForest_v1")
    
    # 4. Вывод с датой
    print("=" * 40)
    print("=== ML Model Report ===")
    print("=" * 40)
    print(f"Date:    {timestamp}")
    print(f"Model:   {report['model']}")
    print(f"Accuracy:  {report['accuracy']}")
    print(f"Precision: {report['precision']}")
    print("=" * 40)
    
    # 5. Логирование завершения
    print(f"\n[INFO] Отчет сгенерирован успешно в {timestamp}")