# -*- coding: utf-8 -*-
"""
Lesson 3: Conditions and Loops — Training Simulation.

Третий урок курса ML Zero to Hero.
Демонстрация работы с условиями, циклами и симуляции обучения
с ранней остановкой (Early Stopping).

Author: Dmitry
Date: 2025
GitHub: https://github.com/mitjagagin/ml-zero-to-hero
"""

from datetime import datetime


# =============================================================================
# КОНСТАНТЫ
# =============================================================================
DEFAULT_LOSS_HISTORY: list[float] = [0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0.05]
TARGET_LOSS_THRESHOLD: float = 0.25  # Порог loss для остановки обучения


# =============================================================================
# ФУНКЦИИ
# =============================================================================
def simulate_training(
    loss_history: list[float],
    target_threshold: float = TARGET_LOSS_THRESHOLD
) -> tuple[bool, int]:
    """
    Симулирует процесс обучения с ранней остановкой.
    
    Args:
        loss_history: Список значений loss по эпохам.
        target_threshold: Целевой порог loss для остановки.
    
    Returns:
        tuple[bool, int]: (достигнут_ли_порог, номер_эпохи_остановки).
    """
    for i, loss in enumerate(loss_history):  # enumerate() даёт индекс и значение
        epoch_number: int = i + 1  # Нумерация эпох с 1 (для человека)
        print(f"Эпоха: {epoch_number} -> Loss: {loss:.4f}")
        
        if loss < target_threshold:
            print(f"✓ Достигнута целевая точность! Останавливаем обучение.")
            return True, epoch_number  # Ранний выход из функции
    
    return False, len(loss_history)  # Если порог не достигнут


def calculate_average_loss(loss_history: list[float]) -> float:
    """
    Вычисляет среднее значение loss по всем эпохам.
    
    Args:
        loss_history: Список значений loss.
    
    Returns:
        float: Среднее значение loss.
    """
    return sum(loss_history) / len(loss_history)


def print_training_report(
    is_target_reached: bool,
    stop_epoch: int,
    avg_loss: float
) -> None:
    """
    Выводит итоговый отчет об обучении.
    
    Args:
        is_target_reached: Флаг достижения целевого порога.
        stop_epoch: Номер эпохи остановки.
        avg_loss: Среднее значение loss.
    """
    print("\n" + "=" * 50)
    print("ИТОГОВЫЙ ОТЧЕТ ПО ОБУЧЕНИЮ")
    print("=" * 50)
    print(f"Остановка на эпохе: {stop_epoch}")
    print(f"Средний Loss: {avg_loss:.4f}")
    print("-" * 50)
    
    if is_target_reached:
        print("✓ Модель готова")
    else:
        print("⚠ Нужно больше эпох")
    
    print("=" * 50)


# =============================================================================
# ТОЧКА ВХОДА
# =============================================================================
if __name__ == "__main__":
    # Загрузка истории обучения (симуляция)
    loss_history: list[float] = DEFAULT_LOSS_HISTORY.copy()
    
    print("=" * 50)
    print("СИМУЛЯЦИЯ ОБУЧЕНИЯ МОДЕЛИ (EARLY STOPPING)")
    print("=" * 50)
    print()
    
    # Запуск симуляции обучения
    is_target_reached: bool
    stop_epoch: int
    is_target_reached, stop_epoch = simulate_training(loss_history)
    
    # Расчет среднего loss
    avg_loss: float = calculate_average_loss(loss_history)
    
    # Вывод итогового отчета
    print_training_report(is_target_reached, stop_epoch, avg_loss)
    
    # Логирование выполнения
    print(f"\n[INFO] Скрипт выполнен успешно в {datetime.now().strftime('%H:%M:%S')}")