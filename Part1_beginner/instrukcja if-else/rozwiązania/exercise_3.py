
# Zapytaj użytkownika o jego oceny końcowe z kilku przedmiotów (matematyka, fizyka, itd.).
# Następnie przeanalizuj je i wypisz informacje czy zdał/zdała do następnej klasy.
# Załóż, że zdać można wtedy jeżeli nie ma się żadnej jedynki
# albo jeżeli ma się jedną jedynkę ale średnia ze wszystkich ocen jest wyższa niż 3.5

# Zapytaj użytkownika o jego oceny końcowe z kilku przedmiotów (matematyka, fizyka, itd.).
# Następnie przeanalizuj je i wypisz informacje czy zdał/zdała do następnej klasy.
# Załóż, że zdać można wtedy jeżeli nie ma się żadnej jedynki
# albo jeżeli ma się jedną jedynkę ale średnia ze wszystkich ocen jest wyższa niż 3.5

math_grade = int(input("Jaka jest Twoja ocena końcowa z matematyki? "))
physics_grade = int(input("Jaka jest Twoja ocena końcowa z fizyki? "))
polish_grade = int(input("Jaka jest Twoja ocena końcowa z języka polskiego? "))
english_grade = int(input("Jaka jest Twoja ocena końcowa z języka angielskiego? "))
history_grade = int(input("Jaka jest Twoja ocena końcowa z historii? "))

number_of_failures = 0

if math_grade < 2:
    number_of_failures = number_of_failures + 1

if physics_grade < 2:
    number_of_failures = number_of_failures + 1

if polish_grade < 2:
    number_of_failures = number_of_failures + 1

if english_grade < 2:
    number_of_failures = number_of_failures + 1

if history_grade < 2:
    number_of_failures = number_of_failures + 1


if number_of_failures == 0:
    print("Gratuluję! Zdałeś/zdałaś do następnej klasy :)")
else:
    if number_of_failures == 1:
        average = (math_grade + physics_grade + polish_grade + english_grade + history_grade) / 5
        if average > 3.5:
            print("Gratuluję! Zdałeś/zdałaś do następnej klasy :)")
        else:
            print("Niestety...")
    else:
        print("Niestety...")
