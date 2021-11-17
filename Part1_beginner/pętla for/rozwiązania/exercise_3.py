
# Wczytaj od użytkownika kolejne kategorie wydatków oraz dla każdej z nich dokonane wydatki
# (zastosuj pętle while do aby użytkownik mógł zakończyć wprowadzanie kategorii i wydatków).
# Stosując pętle for oblicz procentowy udział każdego z wydatków w miesięcznym budżecie
# i wypisz wyniki oraz dodatkowo która kategoria jest najbardziej znacząca.

# W poprzednim rozwiązaniu tego zadania musieliśmy mieć "sztywną" listę kategorii

print("Kalkulator budżetu miesięcznego")
expenditures = {}

category_name = input("Podaj kategorię wydatków albo zakończ wpisując 'X': ")
while category_name != 'X':
    expenditures[category_name] = []
    expenditure = input(f"Podaj wartość następnego wydatku w kategorii {category_name} albo zakończ wpisując 'X': ")
    while expenditure != 'X':
        expenditure_value = float(expenditure)
        expenditures[category_name].append(expenditure_value)
        expenditure = input(f"Podaj wartość następnego wydatku w kategorii {category_name} albo zakończ wpisując 'X': ")
    category_name = input("Podaj kategorię wydatków albo zakończ wpisując 'X': ")


total_expenditures = 0
for category_expenditures in expenditures.values():
    for expenditure_value in category_expenditures:
        total_expenditures += expenditure_value
    # total_expenditures += sum(category_expenditures)


expenditures_percentage = {}
for category_name, category_expenditures in expenditures.items():
    total_category_expenditures = 0
    for expenditure_value in category_expenditures:
        total_category_expenditures += expenditure_value
    # total_category_expenditures = sum(category_expenditures)
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
