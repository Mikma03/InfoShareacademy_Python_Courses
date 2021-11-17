
# Instrukcja in pozwala sprawdzić czy litera występuje w napisie
# name = "Ala"
# if "A" in name:
#     print("W imieniu jest A!")
# else:
#     print("Nie ma A...")


# Możemy za jej pomocą sprawdzić czy element występuje na liście
favourite_sports = ["bieganie", "jazda na rowerze", "pływanie"]
#
# if "koszykówka" in favourite_sports:
#     print("Zagramy w kosza?")
# else:
#     print("Hmm...")

# Oraz czy klucz występuje w słowniku
# person = {
#     "first_name": "Mikołaj",
#     "last_name": "Lewandowski",
# }
# if "first_name" in person:
#     print(person["first_name"])
#
# if "car" in person:
#     print(person["car"])

# Oczywiście działa również negacja
if "koszykówka" not in favourite_sports:
    print("Nie lubisz koszykówki?")
else:
    print("Hmm...")
