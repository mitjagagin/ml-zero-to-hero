# -*- coding: utf-8 -*-
"""
Lesson 9: Scikit-learn — First ML Models.

Девятый урок курса ML Zero to Hero.
Демонстрация обучения модели классификации с помощью Scikit-learn.

Author: Dmitry
Date: 2025
GitHub: https://github.com/mitjagagin/ml-zero-to-hero
"""

from datetime import datetime
from typing import Any

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.preprocessing import LabelEncoder


# =============================================================================
# КОНСТАНТЫ
# =============================================================================
RANDOM_STATE: int = 42
TEST_SIZE: float = 0.2
TARGET_COLUMN: str = "churn"


# =============================================================================
# ФУНКЦИИ ЗАГРУЗКИ ДАННЫХ
# =============================================================================
def load_data(filepath: str) -> pd.DataFrame:
    """
    Загружает данные из CSV файла.
    """
    df: pd.DataFrame = pd.read_csv(filepath)
    print(f"[INFO] Загружено {len(df)} строк")
    return df


# =============================================================================
# ФУНКЦИИ ПРЕДОБРАБОТКИ
# =============================================================================
def preprocess_data(
    df: pd.DataFrame
) -> tuple[np.ndarray, np.ndarray, LabelEncoder]:
    """
    Предобрабатывает данные для обучения.
    """
    encoder: LabelEncoder = LabelEncoder()
    df_processed: pd.DataFrame = df.copy()
    
    df_processed["city_encoded"] = encoder.fit_transform(df_processed["city"])
    df_processed["department_encoded"] = encoder.fit_transform(
        df_processed["department"]
    )
    
    feature_columns: list[str] = [
        "age",
        "salary",
        "city_encoded",
        "department_encoded"
    ]
    
    X: np.ndarray = df_processed[feature_columns].values
    y: np.ndarray = df_processed[TARGET_COLUMN].values
    
    print(f"[INFO] Признаки: {feature_columns}")
    print(f"[INFO] Форма X: {X.shape}, Форма y: {y.shape}")
    
    return X, y, encoder


# =============================================================================
# ФУНКЦИИ ОБУЧЕНИЯ
# =============================================================================
def train_model(
    X_train: np.ndarray,
    y_train: np.ndarray
) -> RandomForestClassifier:
    """
    Обучает модель Random Forest.
    """
    model: RandomForestClassifier = RandomForestClassifier(
        n_estimators=100,
        max_depth=5,
        random_state=RANDOM_STATE
    )
    
    model.fit(X_train, y_train)
    print("[INFO] Модель обучена")
    
    return model


# =============================================================================
# ФУНКЦИИ ОЦЕНКИ
# =============================================================================
def evaluate_model(
    model: RandomForestClassifier,
    X_test: np.ndarray,
    y_test: np.ndarray
) -> dict[str, float]:
    """
    Оценивает качество модели.
    """
    y_pred: np.ndarray = model.predict(X_test)
    
    metrics: dict[str, float] = {
        "accuracy": float(accuracy_score(y_test, y_pred)),
        "precision": float(precision_score(y_test, y_pred, zero_division=0)),
        "recall": float(recall_score(y_test, y_pred, zero_division=0)),
        "f1_score": float(f1_score(y_test, y_pred, zero_division=0))
    }
    
    return metrics


# =============================================================================
# ОСНОВНОЙ ПАЙПЛАЙН
# =============================================================================
def run_pipeline(data_path: str) -> dict[str, Any]:
    """
    Запускает полный ML-пайплайн.
    """
    print("=" * 60)
    print("ЗАПУСК ML ПАЙПЛАЙНА (Scikit-learn)")
    print("=" * 60)
    print()
    
    df: pd.DataFrame = load_data(data_path)
    
    X: np.ndarray
    y: np.ndarray
    encoder: LabelEncoder
    X, y, encoder = preprocess_data(df)
    
    X_train: np.ndarray
    X_test: np.ndarray
    y_train: np.ndarray
    y_test: np.ndarray
    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=TEST_SIZE,
        random_state=RANDOM_STATE,
        stratify=y
    )
    
    print(f"[INFO] Train: {len(X_train)} строк, Test: {len(X_test)} строк")
    print()
    
    model: RandomForestClassifier = train_model(X_train, y_train)
    print()
    
    metrics: dict[str, float] = evaluate_model(model, X_test, y_test)
    
    print("=" * 60)
    print("РЕЗУЛЬТАТЫ МОДЕЛИ")
    print("=" * 60)
    print(f"Accuracy:  {metrics['accuracy']:.1%}")
    print(f"Precision: {metrics['precision']:.1%}")
    print(f"Recall:    {metrics['recall']:.1%}")
    print(f"F1-Score:  {metrics['f1_score']:.1%}")
    print("=" * 60)
    
    return {
        "model": model,
        "metrics": metrics,
        "encoder": encoder
    }


# =============================================================================
# ТОЧКА ВХОДА
# =============================================================================
if __name__ == "__main__":
    run_pipeline(data_path="src/data_employees.csv")
    
    print(f"\n[INFO] Завершено в {datetime.now().strftime('%H:%M:%S')}")