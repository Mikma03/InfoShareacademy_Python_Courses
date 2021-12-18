
# Słownik polsko angielski
polish_to_english = {
    "amnezja": "amnesia",
    "aktywista": "activist",
    "burza": "storm"
}

# print("Słownik polsko angielski:", polish_to_english)

# Dostęp za pomocą klucza
# print(f"Po polsku 'burza' to po angielsku '{polish_to_english['burza']}'")

# Pusty słownik
# empty = {}
# print("Pusty słownik:", empty)

# Wartości mogą być różnych typów
# expenditures = {
#     "prąd": 250,
#     "woda": 30.45,
#     "zakupy": [
#         120.15,
#         170.53,
#         20.15
#     ]
# }
# print(expenditures)

# Dobrą praktyką jest stosowanie jednej konwencji
# expenditures = {
#     "prąd": [250],
#     "woda": [30.45],
#     "zakupy": [
#         120.15,
#         170.53,
#         20.15
#     ]
# }
# print(expenditures)

# Typy int oraz float też mogą być kluczem
# expenditures = {
#     250: "prąd",
#     30.45: "woda",
#     120.15: "zakupy",
#     170.53: "zakupy",
#     20.15: "zakupy"
# }
# print(expenditures)

# Wartości mogą się powtarzać w słowniku ale klucze nie
# expenditures = {
#     250: "prąd",
#     30.45: "woda",
#     250: "zakupy",
# }
# print(expenditures)


# Słowniki mogą zawierać inne słowniki
# teacher = {
#     "first_name": "Jan",
#     "last_name": "Kowalski",
#     "age": 45,
#     "contract": {
#         "sign_date": "23-11-2018",
#         "salary": 3500
#     }
# }
# print(teacher)

# Tak jak słownik może zawierać listy, tak lista może zawierać słownik
students = [
    {
        "first_name": "Patryk",
        "last_name": "Nowak"
    },
    {
        "first_name": "Alicja",
        "last_name": "Kowalska"
    }
]
print(students)
print(students[0])
print(students[1])
print(students[1]['first_name'])
