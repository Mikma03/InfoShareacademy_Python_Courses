
# Za pomocą None możemy wyrazić NIC
# Wartość None możemy przypisać do zmiennej
nothing = None
# print(f"Nic: {nothing}")

# None ma typ NoneType
# print(f"None jest typu: {type(None)}")

# None możemy użyć jako wartość w słowniku
# people = [
#     {
#         "first_name": "Alicja",
#         "car": {
#             "brand": "Ford",
#             "production_year": 2015
#         }
#     },
#     {
#         "first_name": "Jakub",
#         "car": None
#     }
# ]
# print(people)

# None może być elementem na liście
# something = [1, 4, 6, None, 8]
# print(something)

# Na None nie możemy wykonywać operacji arytmetycznych, łączyć bezpośrednio z napisami itd.
# wrong = 3 + None
# wrong = "Napis" + None

# Nie możemy zamienić None na liczbę ani listę
# wrong = int(None)
# wrong = float(None)
# wrong = list(None)

# None konwertuje się jednak na stringa jako napis "None"
# none_str = str(None)
# print("abc" + none_str)
