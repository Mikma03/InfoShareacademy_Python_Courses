
# Zmodyfikuj zadanie dotyczące budżetu domowego “zamykając” spójne elementy programu w funkcje.

print("Kalkulator budżetu miesięcznego")

def load_expenditures(category_name):
    expenditures_values = []
    while True:

        expenditure = input(f"Podaj wartość następnego wydatku w kategorii {category_name} albo zakończ wpisując 'X': ")
        if expenditure == "X":
            return expenditures_values

        expenditure_value = float(expenditure)
        expenditures_values.append(expenditure_value)


def load_expenditures_by_categories():
    expenditures = {}
    while True:
        category_name = input("Podaj kategorię wydatków albo zakończ wpisując 'X': ")
        if category_name == "X":
            return expenditures

        expenditures[category_name] = load_expenditures(category_name)


def calculate_total_expenditures(expenditures):
    result = 0
    for category_expenditures in expenditures.values():
        result += sum(category_expenditures)
    return result


def calculate_expenditures_percentages(expenditures, total_expenditures):
    percentages_by_category_name = {}
    for category_name, category_expenditures in expenditures.items():
        total_category_expenditures = sum(category_expenditures)
        percentages_by_category_name[category_name] = total_category_expenditures * 100 / total_expenditures
    return percentages_by_category_name


def find_most_important_category(percentages_by_category_name):
    highest_percentage_category = None
    highest_percentage = 0
    for category, percentage in percentages_by_category_name.items():
        if percentage > highest_percentage:
            highest_percentage = percentage
            highest_percentage_category = category
    return highest_percentage_category, highest_percentage


def print_most_important_category_info(category_name, percentage):
    print(f"Najwięcej wydajesz na {category_name} - {percentage:.0f}% wszystkich wydatków")


def print_category_info(category, percentage):
    print(f"Na {category} wydajesz {percentage:.0f}% miesięcznych wydatków")


expenditures_by_categories = load_expenditures_by_categories()
total_expenditures = calculate_total_expenditures(expenditures_by_categories)
expenditures_percentage = calculate_expenditures_percentages(expenditures_by_categories)
most_important_category, most_important_category_percentage = find_most_important_category(expenditures_percentage)

if most_important_category is not None:
    print_most_important_category_info(most_important_category, most_important_category_percentage)

for category, percentage in expenditures_percentage.items():
    print_category_info(category, percentage)
