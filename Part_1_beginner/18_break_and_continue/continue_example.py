
# Wypisywanie co drugiego sportu
favourite_sports = ["bieganie", "pływanie", "jazda na rowerze", "triathlon"]
for index, sport in enumerate(favourite_sports):
    if index % 2 != 0:
        continue
    print(sport)
