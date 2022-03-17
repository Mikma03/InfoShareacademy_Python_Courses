
# Zmodyfikuj rozwiązanie zadania z kalkulatorem wydatków
# (lekcja dotycząca słownika w module 3).
# Pobierz te same informacje na temat miesięcznych wydatków
# w różnych kategoriach jednak wypisz informacje
# na temat procentowego udziału jednej najbardziej znaczącej kategorii.

print("Ile miesięcznie wydajesz na")
food = float(input("jedzenie? "))
fun = float(input("rozrywkę? "))
bills = float(input("opłaty? "))
other = float(input("inne? "))

total_expenditures = food + fun + bills + other
expenditures_percentage = {
    "jedzenie": food * 100 / total_expenditures,
    "rozrywka": fun * 100 / total_expenditures,
    "opłaty": bills * 100 / total_expenditures,
    "inne": other * 100 / total_expenditures,
}

most_important_category = "jedzenie"

if expenditures_percentage["rozrywka"] > expenditures_percentage[most_important_category]:
    most_important_category = "rozrywka"

if expenditures_percentage["opłaty"] > expenditures_percentage[most_important_category]:
    most_important_category = "opłaty"

if expenditures_percentage["inne"] > expenditures_percentage[most_important_category]:
    most_important_category = "inne"

print(f"Najwięcej wydajesz na {most_important_category} - {expenditures_percentage[most_important_category]:.0f}% wszystkich wydatków")
