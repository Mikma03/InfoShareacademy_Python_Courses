# Zapytaj użytkownika gdzie mieszka i wypisz odpowiedź, np. "Jak miło że mieszkasz w Gdańsku".
# W razie nieuwagi użytkownika popraw wprowadzoną nazwę miasta
# tak by zaczynała się z wielkiej litery ;)

city = input("W jakim mieście mieszkasz? ")
city = city.title()

print(f"Jak miło, że mieszkasz w {city}!")
