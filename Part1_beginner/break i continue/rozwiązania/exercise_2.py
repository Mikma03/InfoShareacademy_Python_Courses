
# Zmodyfikuj rozwiązanie zadania trzeciego z lekcji dotyczącej pętli for (obliczanie wydatków domowych).
# Skorzystaj z instrukcji break aby wyeliminować powtórzone wywołania funkcji input.


print("Kalkulator budżetu miesięcznego")
expenditures = {}

while True:
    category_name = input("Podaj kategorię wydatków albo zakończ wpisując 'X': ")
    if category_name == "X":
        break
    expenditures[category_name] = []

    while True:
        expenditure = input(f"Podaj wartość następnego wydatku w kategorii {category_name} albo zakończ wpisując 'X': ")
        if expenditure == "X":
            break

        expenditure_value = float(expenditure)
        expenditures[category_name].append(expenditure_value)


total_expenditures = 0
for category_expenditures in expenditures.values():
    total_expenditures += sum(category_expenditures)


expenditures_percentage = {}
for category_name, category_expenditures in expenditures.items():
    total_category_expenditures = sum(category_expenditures)
    expenditures_percentage[category_name] = total_category_expenditures * 100 / total_expenditures

most_important_category = None
most_important_category_percentage = 0
for category, percentage in expenditures_percentage.items():
    if percentage > most_important_category_percentage:
        most_important_category_percentage = percentage
        most_important_category = category

if most_important_category is not None:
    print(f"Najwięcej wydajesz na {most_important_category} - {most_important_category_percentage:.0f}% wszystkich wydatków")

for category, percentage in expenditures_percentage.items():
    print(f"Na {category} wydajesz {percentage:.0f}% miesięcznych wydatków")
