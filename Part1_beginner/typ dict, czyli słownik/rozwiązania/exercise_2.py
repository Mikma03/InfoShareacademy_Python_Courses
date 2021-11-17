
# Stwórz zmienną my_family zawierającą drzewo genealogiczne twojej rodziny.
# Zacznij od siebie - opisując imię, nazwisko, datę urodzenia
# każdej osoby oraz jej rodziców.
# Podpowiedź: rodzice będą listami, zawierającymi w sobie kolejne słowniki.

my_family = {
    "first_name": "Mikołaj",
    "last_name": "Lewandowski",
    "birth_date": "23-11-1991",
    "parents": [
        {
            "first_name": "Jan",
            "last_name": "Lewandowski",
            "birth_date": "15-11-1961",
            "parents": [
                {
                    "first_name": "Piotr",
                    "last_name": "Lewandowski",
                    "birth_date": "15-11-1931",
                    "parents": [],
                },
                {
                    "first_name": "Beata",
                    "last_name": "Lewandowska",
                    "birth_date": "15-11-1931",
                    "parents": [],
                },
            ]
        },
        {
            "first_name": "Alicja",
            "last_name": "Lewandowski",
            "birth_date": "15-11-1961",
            "parents": [
                {
                    "first_name": "Paweł",
                    "last_name": "Kowalski",
                    "birth_date": "15-11-1931",
                    "parents": [],
                },
                {
                    "first_name": "Anna",
                    "last_name": "Kowalska",
                    "birth_date": "15-11-1931",
                    "parents": [],
                },
            ]

        }
    ],
}
print("Drzewo genealogiczne", my_family)
