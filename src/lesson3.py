# создаем список
loss_history = [0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0.05]

# Выводим список
for i, loss in enumerate(loss_history):
    print(f"Эпоха: {i + 1} -> Loss: {loss}")
    if loss < 0.25:
        print(f"Достигнута целевая точность! Останавливаем обучение.")
        break

# Проверка
if loss < 0.25:
    print(f"Модель готова")
else:
    print(f"Нужно больше эпох")

# Средний Loss
avg_loss = sum(loss_history) / len(loss_history)
print(f"Средний Loss: {avg_loss:.4f}")  # :.4f округляет до 4 знаков