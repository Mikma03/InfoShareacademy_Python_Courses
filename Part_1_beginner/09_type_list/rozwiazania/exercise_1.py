
# Stwórz zmienną favourite_sports, która będzie listą
# zawierającą nazwy dyscyplin sportu, które lubisz.
# Następnie wypisz informacje,
# jaki sport jest pierwszy na Twojej liście a jaki ostatni.
# Podmień jeden ze sportów na inny i wypisz całą listę.

favourite_sports = [
    "bieganie",
    "jazda na rowerze",
    "pływanie"
]

print("Moim ulubionym sportem jest:", favourite_sports[0])
print("Lubię też:", favourite_sports[-1])

favourite_sports[-1] = "triathlon"
print("Zmieniłem zdanie -> moje ulubione sporty to:", favourite_sports)
