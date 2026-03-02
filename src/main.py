# Импортируем свои функции из модуля metrics
from metrics import get_model_report

# Импортируем стандартный модуль для работы с датой
from datetime import datetime

if __name__ == "__main__":
    # Получаем текущую дату и время
    now = datetime.now()
    
    # Данные для теста
    y_true = [1, 0, 1, 1, 0, 1, 0, 0]
    y_pred = [1, 0, 0, 1, 0, 1, 1, 0]
    
    # Получаем отчет
    report = get_model_report(y_true, y_pred, model_name="RandomForest_v1")
    
    # Вывод с датой
    print(f"=== ML Model Report ===")
    print(f"Date: {now.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Model: {report['model']}")
    print(f"Accuracy: {report['accuracy']}")
    print(f"Precision: {report['precision']}")