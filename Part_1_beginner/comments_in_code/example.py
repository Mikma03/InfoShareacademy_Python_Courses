
# Program do obliczenia wartości lokaty z roczną kapitalizacją
initial_value = 2000  # To też jest komentarz
percentage = 5
years = 7

# Wartość lokaty obliczana zgodnie z wzorem na procent składany
final_value = initial_value * (1 + percentage / 100) ** years

print("Po", years, "latach Twoja lokata będzie warta", final_value)
