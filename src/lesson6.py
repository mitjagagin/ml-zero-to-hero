import csv
import json

data = []
with open("data.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        data.append(row)

total = len(data)
avg_age = 0
avg_salary = 0
churn_rate = 0
rows = 0

for row in data:
    avg_age = avg_age + int(row["age"])
    avg_salary = avg_salary + float(row["salary"])
    churn_rate = churn_rate + int(row["churn"])
    rows += rows

report = {
    "total_records": total,
    "avg_age": avg_age / total,
    "avg_salary": avg_salary / total,
    "churn_rate": (churn_rate / total) * 100
}

with open("report.json", "w", encoding="utf-8") as file:
    json.dump(report, file, indent=4, ensure_ascii=False)

print("Отчет сохранен в report.json")