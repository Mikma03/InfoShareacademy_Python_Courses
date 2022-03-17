
# Lista smaków
favourite_flavours = [
    "malinowy",         # 0
    "truskawkowy",      # 1
    "czekoladowy",      # 2
    "pistacjowy",       # 3
    "kokosowy",         # 4
]
print(favourite_flavours)
# Lubię być zapobiegawczy - dodam jeszcze jeden smak awaryjny
favourite_flavours.append("kawowy")
print(favourite_flavours)

# Dodanie elementu w dowolnym miejscu - np. na początku
favourite_flavours.insert(0, "jagodowy")
print(favourite_flavours)

# Usunięcie elementu po indeksie
del favourite_flavours[4]
print(favourite_flavours)

# Wyciągnięcie elementu z listy po indeksie
second_flavour = favourite_flavours.pop(1)
print(second_flavour)
print(favourite_flavours)

# Usunięcie elementów po wartości
favourite_flavours.remove("czekoladowy")
print(favourite_flavours)

# Podmiana elementu
favourite_flavours[-1] = "malinowy"
print(favourite_flavours)

# Nie można dodać/podmienić elementu, który nie istniał wcześniej
favourite_flavours[45] = "cytrynowy"
print(favourite_flavours)
