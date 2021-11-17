
# Zapytaj użytkownika o ceny trzech produktów i wypisz wyniki ich porównania

computer_price = float(input("Ile średnio kosztuje komputer? "))
car_price = float(input("Ile kosztuje typowy samochód? "))
bike_price = float(input("Ile kosztuje typowy rower? "))

print(f"Czy komputer jest droższy od samochodu? {computer_price > car_price}")
print(f"Czy rower jest tańszy od komputera? {bike_price < computer_price}")
print(f"Czy samochód kosztuje tyle samo co rower? {car_price == bike_price}")

