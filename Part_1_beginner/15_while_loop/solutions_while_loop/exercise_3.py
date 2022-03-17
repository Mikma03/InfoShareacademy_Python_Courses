
# Poproś o użytkownika o podanie ulubionych dań, rozdzielając każde z nich przecinkiem.
# Następnie wypisz każde z nich wraz z informacją, które miejsce zajmuje na jego/jej liście.

dishes = input("Podaj swoje ulubione dania, rozdzielając je przecinkiem: ")
favourite_dishes = dishes.split(",")

dish_index = 0
while dish_index < len(favourite_dishes):
    print(f"Ulubione danie numer {dish_index}: {favourite_dishes[dish_index]}")
    dish_index += 1
