
# Ten sam warunek zapisany za pomocą operatora and
# name = input("Jak się nazywasz? ")
# print(f"Miło Cię poznać {name}")
# name_length = len(name)

# if name_length < 5:
#     print(f"{name} to raczej krótkie imię")
# if name_length >= 5 and name_length <= 8:
#     print(f"{name} to imię zwykłej długości!")
# else:
#     print(f"{name} to długie imie!")

# if name_length < 5:
#     print(f"{name} to raczej krótkie imię")
# if 5 <= name_length <= 8:
#     print(f"{name} to imię zwykłej długości!")
# else:
#     print(f"{name} to długie imie!")

born_as_usa_citizen_answer = input("Czy jesteś obywatelem USA od urodzenia? (T/N) ")
age = int(input("Ile masz lat? "))
usa_residence_years = int(input("Ile lat mieszkasz w USA? "))

if born_as_usa_citizen_answer == "T":
    born_as_usa_citizen = True
else:
    born_as_usa_citizen = False

if born_as_usa_citizen and age >= 35 and usa_residence_years >= 14:
    print("Możesz kandydować")
else:
    print("Nie możesz kandydować")
