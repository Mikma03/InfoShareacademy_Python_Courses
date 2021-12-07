
# Za pomocą pętli for możemy wypisać klucze ze słownika
expenditures = {
    "prąd": [250],
    "woda": [30.45],
    "zakupy": [
        120.15,
        170.53,
        20.15
    ]
}
# for expenditure_name in expenditures:
#     print(expenditure_name)

# Klucze i wartości
# for expenditure_name in expenditures:
#     print(f"{expenditure_name} -> {expenditures[expenditure_name]}")

# Wartości
# for expenditure in expenditures.values():
#     print(expenditure)

# Klucze i wartości - bezpośrednio
# for expenditure_name, expenditure in expenditures.items():
#     print(f"{expenditure_name} -> {expenditure}")

# for item in expenditures.items():
    # print(item)
    # print(f"{item[0]} -> {item[1]}")
    # print(type(item))

# Nie można zmodyfikować elementów krotki:
# item = ("prąd", 340)
# item[1] = 20

# Krotkę można "rozpakować"
# item = ("prąd", 340)
# name, value = item
# print(name, value)

