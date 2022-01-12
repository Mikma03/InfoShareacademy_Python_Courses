
# Napisz kalkulator dla kredytu o malejącej racie. Zapytaj użytkownika o:
# -> Kwotę kredytu
# -> Oprocentowanie kredytu
# -> Czas trwania (w latach)
# -> Koszty początkowe (prowizja itp.)
# Oblicz jaką łącznie sumę użytkownik odda bankowi i porównaj ją z kapitałem, który otrzyma.
# Podpowiedź: oblicz wartość każdej miesięcznej raty według wzoru:
# kapitał spłacany miesięcznie = kwota kredytu / (liczba lat * 12)
# pozostały kapitał = kwota kredytu - (numer miesiąca od początku - 1) * kapitał spłacany miesięcznie
# rata = (pozostały kapitał * oprocentowanie / 100) / 12 + kapitał spłacany miesięcznie

capital = int(input("Na jaką kwotę jest kredyt? "))
interest_rate = float(input("Jakie jest oprocentowanie (%)? "))
years = int(input("Na ile lat jest kredyt? "))
initial_fees = int(input("Jakie są koszty początkowe? "))

credit_time_in_months = years * 12
monthly_paid_capital = capital / credit_time_in_months
total_paid = initial_fees
for month_number in range(1, credit_time_in_months + 1):
    capital_to_be_paid = capital - (month_number - 1) * monthly_paid_capital
    installment = (capital_to_be_paid * interest_rate / 100) / 12 + monthly_paid_capital
    total_paid += installment
    print(f"Rata w miesiącu {month_number} wyniesie {installment:.2f}")

print(f"Zaciągając {capital} na tych warunkach spłacisz z odsetkami {total_paid}")
