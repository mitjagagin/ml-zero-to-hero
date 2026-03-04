# -*- coding: utf-8 -*-
"""
Название модуля.

Описание назначения модуля.

Author: Dmitry
Date: 2025
GitHub: https://github.com/mitjagagin/ml-zero-to-hero
"""

from datetime import datetime
from typing import Any, Dict, List


# =============================================================================
# КОНСТАНТЫ
# =============================================================================
DEFAULT_VALUE: str = "default"


# =============================================================================
# ФУНКЦИИ
# =============================================================================
def process_data(data: List[int]) -> Dict[str, float]:
    """
    Обрабатывает входные данные.
    
    Args:
        data: Список чисел.
    
    Returns:
        Словарь со статистикой.
    """
    if not data:
        return {}
    
    return {
        "mean": sum(data) / len(data),
        "max": max(data),
        "min": min(data)
    }


# =============================================================================
# ТОЧКА ВХОДА
# =============================================================================
if __name__ == "__main__":
    print("[INFO] Тестирование модуля...")
    test_data: List[int] = [1, 2, 3, 4, 5]
    result: Dict[str, float] = process_data(test_data)
    print(f"Результат: {result}")
    print(f"\n[INFO] Завершено в {datetime.now().strftime('%H:%M:%S')}")