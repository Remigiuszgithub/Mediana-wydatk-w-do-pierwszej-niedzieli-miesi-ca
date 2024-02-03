from statistics import median
from datetime import datetime, timedelta

def get_median_of_first_week_expenses(expenses):
    result = {}

    for month, days in expenses.items():
        week_expenses = []

        # Znajdź datę pierwszej niedzieli w danym miesiącu
        if not days:
            result[f"mediana dla {month}"] = "Brak wydatków"
            continue

        # Posortuj dni w danym miesiącu
        sorted_days = sorted(days.keys())
        first_day = sorted_days[0]
        first_sunday = datetime.strptime(f"{month}-{first_day}", "%Y-%m-%d")
        while first_sunday.weekday() != 6:  # 6 oznacza niedzielę
            first_sunday += timedelta(days=1)

        # Dodawaj wydatki do pierwszej niedzieli
        for day in sorted_days:
            categories = days[day]
            date_obj = datetime.strptime(f"{month}-{day}", "%Y-%m-%d")
            if date_obj > first_sunday:
                break
            for category_values in categories.values():
                week_expenses.extend(category_values)

        # Oblicz medianę dla danego miesiąca
        result[f"mediana dla {month}"] = str(median(week_expenses)) if week_expenses else "Brak wydatków"

    return result

# Przykładowe dane
expenses = {
    "2023-01": {
        "01": {
            "food": [22.11, 43, 11.72, 2.2, 36.29, 2.5, 19],
            "fuel": [210.22]
        },
        "09": {
            "food": [11.9],
            "fuel": [190.22]
        }
    },
    "2023-03": {
        "07": {
            "food": [20, 11.9, 30.20, 11.9]
        },
        "04": {
            "food": [10.20, 11.50, 2.5],
            "fuel": []
        }
    },
    "2023-04": {}
}

# Wywołaj funkcję
result = get_median_of_first_week_expenses(expenses)

# Wypisz wyniki
for key, value in result.items():
    print(f"{key} = {value}")
