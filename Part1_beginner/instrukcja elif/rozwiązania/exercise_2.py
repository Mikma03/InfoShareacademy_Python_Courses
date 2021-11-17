
# Zaimplementuj program w interpretujący wynik uzyskany w teście Coopera
# (https://pl.wikipedia.org/wiki/Test_Coopera).
# Zapytaj o wiek, płeć i uzyskany wynik i na tej podstawie zinterpretuj rezultat.

age = int(input("Ile masz lat? "))
gender = input("Jesteś mężczyzną czy kobietą? (M/K) ")
result = int(input("Jaki był Twój wynik w teście 12 minut biegu (ile metrów)? "))

if age == 8:
    if gender == "M":
        if result >= 2190:
            print("Bardzo dobrze")
        elif result >= 1810:
            print("Dobrze")
        elif result >= 1420:
            print("Średnio")
        elif result >= 1050:
            print("Źle")
        else:
            print("Bardzo źle")
    else:
        if result >= 2010:
            print("Bardzo dobrze")
        elif result >= 1670:
            print("Dobrze")
        elif result >= 1320:
            print("Średnio")
        elif result >= 990:
            print("Źle")
        else:
            print("Bardzo źle")
elif age == 9:
    if gender == "M":
        if result >= 2350:
            print("Bardzo dobrze")
        elif result >= 1950:
            print("Dobrze")
        elif result >= 1540:
            print("Średnio")
        elif result >= 1130:
            print("Źle")
        else:
            print("Bardzo źle")
    else:
        if result >= 2120:
            print("Bardzo dobrze")
        elif result >= 1770:
            print("Dobrze")
        elif result >= 1400:
            print("Średnio")
        elif result >= 1050:
            print("Źle")
        else:
            print("Bardzo źle")
