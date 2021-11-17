
# Lista smaków
favourite_flavours = [
    "malinowy",         # 0
    "truskawkowy",      # 1
    "czekoladowy",      # 2
    "pistacjowy",       # 3
    "kokosowy",         # 4
]
# print("Ulubiony smak lodów:", favourite_flavours[0])
# print("Drugi smak lodów:", favourite_flavours[1])
# print("Trzeci smak lodów:", favourite_flavours[2])
# print("Czwarty smak lodów:", favourite_flavours[3])
# print("Czwarty smak lodów:", favourite_flavours[4])

# Nieistniejący element
# print("Nieistniejący smak:", favourite_flavours[5])

# Długość listy
# print(f"Na liście jest {len(favourite_flavours)} smaków lodów")

# Ostatni element listy
# print("Ten już nie istnieje:", favourite_flavours[len(favourite_flavours)])
# print("Ostatni element:", favourite_flavours[len(favourite_flavours) - 1])

# Ostatni element listy - wygodniej
# print("Ostatni smak na liście:", favourite_flavours[-1])

# Przedostatni element listy - wygodniej
# print("Ostatni smak na liście:", favourite_flavours[-2])


# favourite_flavours = [
#     "malinowy",         # 0 / -5
#     "truskawkowy",      # 1 / -4
#     "czekoladowy",      # 2 / -3
#     "pistacjowy",       # 3 / -2
#     "kokosowy",         # 4 / -1
# ]

# Pierwszy smak na liście - przekombinowane
# print("Działa ale przekombinowane:", favourite_flavours[-len(favourite_flavours)])
#
# print("Dwa najbardziej ulubione smaki:", favourite_flavours[:2])
#
# print("Wszystkie smaki poza dwoma ulubionymi:", favourite_flavours[2:])

print("Dwa najmniej ulubione smaki:", favourite_flavours[-2:])
