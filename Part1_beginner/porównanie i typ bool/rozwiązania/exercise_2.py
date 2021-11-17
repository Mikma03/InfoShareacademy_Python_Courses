
# Poproś użytkownika o wprowadzenie listy zakupów,
# rozdzielając poszczególne elementy przecinkiem.
# Następnie powiedz (wypisz), czy jest to według Ciebie długa lista czy też nie

shopping_elements = input("Wprowadź listę zakupów, rozdzielając poszczególne elementy przecinkiem: ")
shopping_list = shopping_elements.split(",")

is_shopping_list_long = len(shopping_list) > 4
print(f"Czy uważam, że Twoja lista zakupów jest długa? {is_shopping_list_long}")
