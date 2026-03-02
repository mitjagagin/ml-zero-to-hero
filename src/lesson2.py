# Создаем словарь
training_log = {
    "model_name": "model1",
    "epochs": 100,
    "metrics": [0.2, 0.1, 0.4, 0.3, 0.5]
}

# Выводим данные
print(f"Название модели: {training_log['model_name']}\nПоследняя метрика из списка: {training_log['metrics'][-1]}\nЛучшая метрика: {max(training_log['metrics'])}")

# Новый ключ
training_log["is_trained"] = True

# Выводим словарь построчно
for key, value in training_log.items():
    print(f"{key} -> {value}")