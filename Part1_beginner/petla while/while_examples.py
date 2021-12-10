
# Dopóki licznik nie przekroczy 30 wypisujemy kolejne liczby
# counter = 0
# while counter <= 30:
#     print(counter)
#     counter += 1

# while True:
#     print("Nigdy nie skończę!!!")

# expected_potatoes = int(input("Ile ziemniaków chcesz na obiad? "))
# potatoes = []
# while len(potatoes) < expected_potatoes:
#     print("Obieram ziemniaka...")
#     print("I wrzucam go do garnka :)")
#     potatoes.append("Ziemniak")
# print(potatoes)


# Chcemy żeby liczba podana przez użytkownika była większa niż 100
# number = int(input("Podaj liczbę większą niż 100: "))
# while number <= 100:
#     print(f"{number} nie jest większe niż 100! Spróbujmy jeszcze raz... \n")
#     number = int(input("Podaj liczbę większą niż 100: "))
#
# print(f"Brawo!")

# Możemy upewnić się, że użytkownik podał sensowną wartość
# age = int(input("Ile masz lat? "))
# while age < 1:
#     print("Chyba nie...\n")
#     age = int(input("Ile masz lat? "))
#
# if age < 18:
#     print("Jeszcze nie możesz głosować")
# else:
#     print("Możesz już głosować!")

# Pozwalamy użytkownikowi skorzystać z programu wielokrotnie
option = "T"
while option == "T":
    income = int(input("Podaj przychód: "))
    employees_number = int(input("Podaj liczbę pracowników: "))
    years_on_the_market = int(input("Ile lat działacie na rynku: "))
    if income < 2000:
        print("Przyznano główne wsparcie")
    elif 5 <= employees_number <= 10:
        print("Przyznano wsparcie z funduszu pracowników")
    elif years_on_the_market < 3:
        print("Przyznano wsparcie dla nowych firm")
    else:
        print("Przyznano wsparcie na pocieszenie ;)")

    option = input("Jeżeli chcesz sprawdzić dla innych danych wpisz 'T': ")
