
def calculate_investment_value(initial_value, percentage, years):
    result = initial_value * (1 + percentage / 100) ** years
    return result


def ask_for_int_value(message):
    input_value = input(message)
    return int(input_value)


def run_investment_calculator():
    print("Kalkulator wartości lokaty z roczną kapitalizacją")

    initial_value = ask_for_int_value("Jaką kwotę wpłaciłeś/wpłaciłaś? ")
    percentage = ask_for_int_value("Jakie jest oprocentowanie (%)? ")
    years = ask_for_int_value("Ile lat trwa lokata? ")

    final_value = calculate_investment_value(initial_value, percentage, years)
    print(f"Po {years} latach Twoja lokata będzie warta {final_value:.2f}")

    longer_term = years * 2
    alternative_value = calculate_investment_value(initial_value, percentage, longer_term)
    print(f"Rozważ zostawienie lokaty na {longer_term} lat - będzie wtedy warta {alternative_value:.2f}")


option = None
while option != "X":
    run_investment_calculator()
    option = input("Aby przerwać wprowadź 'X', wpisz inny znak by kontynuować: ")
