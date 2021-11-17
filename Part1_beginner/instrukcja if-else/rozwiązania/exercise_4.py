
# Zapytaj o imię i “rozpoznaj” czy użytkownik to kobieta czy mężczyzna.
# Podpowiedź: Na cele tego zadania możemy założyć, że żeńskie imiona kończą się na “a” :)

name = input("Jak masz na imię? ")

if name[-1] == "a":
    print("Jesteś kobietą")
else:
    print("Jesteś mężczyzną")
