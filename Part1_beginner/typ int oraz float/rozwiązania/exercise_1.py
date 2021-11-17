
# Napisz program, który zapyta użytkownika jaka jest cena jabłek w Biedronce, Lidlu i Żabce.
# Następnie wypisze informacje po ile są najtańsze jabłka.

biedronka_price = float(input("Ile kosztują jabłka w Biedronce? "))
lidl_price = float(input("Ile kosztują jabłka w Lidlu? "))
zabka_price = float(input("Ile kosztują jabłka w Żabce? "))

cheapest_price = min(biedronka_price, lidl_price, zabka_price)

print("Najtańsze jabłka są po:", cheapest_price)
