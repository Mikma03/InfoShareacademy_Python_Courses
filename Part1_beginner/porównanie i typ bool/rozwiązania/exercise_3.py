
# Zmodyfikuj program obliczający wartość lokaty,
# tak aby dodatkowo wypisywał informacje,
# czy w planowanym okresie łączna wartość inwestycji wzrośnie o 10%

print("Kalkulator wartości lokaty z roczną kapitalizacją")

initial_value_input = input("Jaką kwotę wpłaciłeś/wpłaciłaś? ")
initial_value = int(initial_value_input)
percentage_input = input("Jakie jest oprocentowanie (%)? ")
percentage = int(percentage_input)
years_input = input("Ile lat trwa lokata? ")
years = int(years_input)

final_value = initial_value * (1 + percentage / 100) ** years
capital_growth = final_value - initial_value
capital_growth_percentage = (capital_growth / initial_value) * 100

print("Po", years, "latach Twoja lokata będzie warta", final_value)
print(f"Czy wartość Twojej lokaty wzrośnie w tym czasie o 10% lub więcej? {capital_growth_percentage >= 10}")
