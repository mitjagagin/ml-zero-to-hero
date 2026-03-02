# lesson1.py
# Моя первая профессиональная программа

# 1. Объяви переменные о себе
user_name: str = "Dmitry"
learning_goal: str = "Middle ML Engineer"
months_on_vachta: int = 12

# 2. Посчитай сколько это дней (грубо)
day_experience: int = months_on_vachta * 30

# 3. Выведи результат используя f-string
print(f"Привет, я {user_name}. Моя цель: {learning_goal}. Опыт в днях: ~{day_experience}")