# -*- coding: utf-8 -*-
"""
Lesson 3: Conditions and Loops — Training Simulation.

Третий урок курса ML Zero to Hero.
Демонстрация работы с условиями, циклами и симуляции процесса обучения модели
с ранней остановкой (Early Stopping).

Author: Dmitry
Date: 2025
GitHub: https://github.com/mitjagagin/ml-zero-to-hero
"""

from datetime import datetime
from typing import List, Tuple


# =============================================================================
# КОНСТАНТЫ
# =============================================================================
DEFAULT_LOSS_HISTORY: List[float] = [0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0.05]
TARGET_LOSS_THRESHOLD: float = 0.25
DECIMAL_PRECISION: int = 4


# =============================================================================
# ФУНКЦИИ
# =============================================================================
def simulate_training(
    loss_history: List[float],
    target_threshold: float = TARGET_LOSS_THRESHOLD
) -> Tuple[bool, int]:
    """
    Симулирует процесс обучения модели с ранней остановкой.

    Проходит по истории loss и останавливается, когда достигается целевой порог.

    Args:
        loss_history: Список значений loss по эпохам.
        target_threshold: Целевой порог loss для остановки.

    Returns:
        Tuple[bool, int]: Кортеж (достигнут_ли_порог, номер_эпохи_остановки).
    """
    for i, loss in enumerate(loss_history):
        epoch_number: int = i + 1  # Нумерация эпох с 1
        print(f"Эпоха: {epoch_number} -> Loss: {loss:.{DECIMAL_PRECISION}f}")
        
        if loss < target_threshold:
            print(f"✓ Достигнута целевая точность (loss < {target_threshold})! Останавливаем обучение.")
            return True, epoch_number
    
    return False, len(loss_history)


def check_training_status(
    is_target_reached: bool,
    final_loss: float,
    threshold: float = TARGET_LOSS_THRESHOLD
) -> str:
    """
    Проверяет статус обучения и возвращает сообщение.

    Args:
        is_target_reached: Флаг достижения целевого порога.
        final_loss: Финальное значение loss.
        threshold: Целевой порог loss.

    Returns:
        str: Сообщение о статусе обучения.
    """
    if is_target_reached:
        return f"✓ Модель готова (финальный loss: {final_loss:.{DECIMAL_PRECISION}f})"
    else:
        return f"⚠ Нужно больше эпох (финальный loss: {final_loss:.{DECIMAL_PRECISION}f} > {threshold})"


def calculate_average_loss(loss_history: List[float]) -> float:
    """
    Вычисляет среднее значение loss по всем эпохам.

    Args:
        loss_history: Список значений loss по эпохам.

    Returns:
        float: Среднее значение loss.
    """
    return sum(loss_history) / len(loss_history)


def print_training_report(
    loss_history: List[float],
    is_target_reached: bool,
    stop_epoch: int,
    avg_loss: float
) -> None:
    """
    Выводит итоговый отчет об обучении.

    Args:
        loss_history: Список значений loss по эпохам.
        is_target_reached: Флаг достижения целевого порога.
        stop_epoch: Номер эпохи остановки.
        avg_loss: Среднее значение loss.
    """
    print("\n" + "=" * 50)
    print("ИТОГОВЫЙ ОТЧЕТ ПО ОБУЧЕНИЮ")
    print("=" * 50)
    print(f"Всего эпох в истории: {len(loss_history)}")
    print(f"Остановка на эпохе: {stop_epoch}")
    print(f"Средний Loss: {avg_loss:.{DECIMAL_PRECISION}f}")
    print(f"Целевой порог: {TARGET_LOSS_THRESHOLD}")
    print("-" * 50)
    print(check_training_status(is_target_reached, loss_history[stop_epoch - 1]))
    print("=" * 50)


# =============================================================================
# ТОЧКА ВХОДА
# =============================================================================
if __name__ == "__main__":
    # 1. Входные данные (симуляция истории обучения)
    loss_history: List[float] = DEFAULT_LOSS_HISTORY.copy()
    
    print("=" * 50)
    print("СИМУЛЯЦИЯ ОБУЧЕНИЯ МОДЕЛИ (EARLY STOPPING)")
    print("=" * 50)
    print()
    
    # 2. Запуск симуляции обучения
    is_target_reached: bool
    stop_epoch: int
    is_target_reached, stop_epoch = simulate_training(loss_history)
    
    # 3. Расчет среднего loss
    avg_loss: float = calculate_average_loss(loss_history)
    
    # 4. Вывод итогового отчета
    print_training_report(loss_history, is_target_reached, stop_epoch, avg_loss)
    
    # 5. Логирование выполнения
    print(f"\n[INFO] Скрипт выполнен успешно в {datetime.now().strftime('%H:%M:%S')}")