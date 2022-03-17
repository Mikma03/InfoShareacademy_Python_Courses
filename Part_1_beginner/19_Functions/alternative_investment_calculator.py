
def calculate_investment_value(initial_value, percentage, years):
    # result = initial_value * (1 + percentage / 100) ** years
    # return result
    return initial_value * (1 + percentage / 100) ** years

print("Kalkulator wartości lokaty z roczną kapitalizacją")

initial_value_input = input("Jaką kwotę wpłaciłeś/wpłaciłaś? ")
initial_value = int(initial_value_input)
percentage_input = input("Jakie jest oprocentowanie (%)? ")
percentage = int(percentage_input)
years_input = input("Ile lat trwa lokata? ")
years = int(years_input)

############################################################################

final_value = calculate_investment_value(initial_value, percentage, years)
print(f"Po {years} latach Twoja lokata będzie warta {final_value:.2f}")

longer_term = years * 2
alternative_value = calculate_investment_value(initial_value, percentage, longer_term)
print(f"Rozważ zostawienie lokaty na {longer_term} lat - będzie wtedy warta {alternative_value:.2f}")

############################################################################

def say_hello():
    print("Hello World!")


hello_result = say_hello()
print(hello_result)
