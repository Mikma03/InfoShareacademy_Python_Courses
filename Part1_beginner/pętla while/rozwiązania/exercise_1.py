
# Pytaj użytkownika o liczbę tak długo aż poda parzystą albo przekroczy limit 10 prób
number = int(input("Podaj liczbę parzystą: "))
try_number = 1
while try_number < 10 and number % 2 != 0:
    number = int(input("Spróbuj jeszcze raz. Podaj liczbę parzystą: "))
    try_number += 1
