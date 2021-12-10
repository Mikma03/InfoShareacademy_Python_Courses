
# Zapytaj użytkownika o numer telefonu i sprawdź czy zawiera przynajmniej jedną cyfrę 0

phone_number = input("Jaki jest Twój numer telefonu? ")

if "0" in phone_number:
    print("Twój numer zawiera cyfrę zero")
else:
    print("W Twoim numerze nie ma zer")
