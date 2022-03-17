
# Zapytaj użytkownika o 3 ulubione potrawy i zapisz je w postaci listy
# favourite_dishes = []
# dish = input("Jakie jest Twoje ulubione danie nr 1? ")
# favourite_dishes.append(dish)
# dish = input("Jakie jest Twoje ulubione danie nr 2? ")
# favourite_dishes.append(dish)
# dish = input("Jakie jest Twoje ulubione danie nr 3? ")
# favourite_dishes.append(dish)
#
# print("Twoje ulubione dania to:", favourite_dishes)

# Alternatywne rozwiązanie
dishes = input("Jakie są Twoje 3 ulubione dania? Wymień, rozdzielając przecinkiem ")
favourite_dishes = dishes.split(',')
print(favourite_dishes)
