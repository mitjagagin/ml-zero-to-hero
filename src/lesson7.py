import numpy as np

salaries = np.array([50000, 78000, 62000, 90000, 45000, 55000, 82000, 71000])

ages = np.array([25, 34, 29, 45, 23, 28, 38, 31])

avg_salary = np.mean(salaries)
median_salary = np.median(salaries)
max_salary = np.max(salaries)
min_salary = np.min(salaries)
max_index = np.argmax(salaries)
max_salary_age = ages[max_index]
high_salaries = salaries[salaries > 60000]
std_salary = np.std(salaries)

print("=== Анализ зарплат (NumPy) ===")
print(f"Средняя зарплата: {avg_salary}")
print(f"Медианная зарплата: {median_salary}")
print(f"Максимальная зарплата: {max_salary}")
print(f"Минимальная зарплата: {min_salary}")
print(f"Возраст самого высокооплачиваемого: {max_salary_age}")
print(f"Зарплаты > 60000: {high_salaries}")
print(f"Стандартное отклонение: {std_salary}")