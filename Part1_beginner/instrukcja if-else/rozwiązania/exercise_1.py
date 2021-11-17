
# Zapytaj użytkownika o ceny trzech produktów i wypisz wyniki ich porównania

computer_price = float(input("Ile średnio kosztuje komputer? "))
car_price = float(input("Ile kosztuje typowy samochód? "))
bike_price = float(input("Ile kosztuje typowy rower? "))

if computer_price > car_price:
    print("Komputer jest droższy od samochodu")
else:
    print("Komputer jest tańszy od samochodu")

if bike_price < computer_price:
    print("Rower jest tańszy niż komputer")
else:
    print("Rower jest droższy niż komputer")

if car_price == bike_price:
    print("Samochód kosztuje tyle samo co rower")
else:
    print("Samochód nie kosztuje tyle samo co rower")


# Poproś użytkownika o wprowadzenie listy zakupów,
# rozdzielając poszczególne elementy przecinkiem.
# Następnie powiedz (wypisz), czy jest to według Ciebie długa lista czy też nie

shopping_elements = input("Wprowadź listę zakupów, rozdzielając poszczególne elementy przecinkiem: ")
shopping_list = shopping_elements.split(",")

if len(shopping_list) > 4:
    print("Ale długa lista zakupów!")
else:
    print("Taka zwykła lista zakupów")
