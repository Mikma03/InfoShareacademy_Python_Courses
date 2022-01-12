
teacher = {
    "first_name": "Jan",
    "last_name": "Kowalski",
    "age": 45,
    "contract": {
        "sign_date": "23-11-2018",
        "salary": 3500
    }
}
# print(teacher)

# Podobnie jak w przypadku listy możemy modyfikować wartość pod kluczem
# teacher["first_name"] = "Albert"
# print(teacher)

# Nowy klucz dodajemy w ten sam sposób (co nie zadziała  w przypadku listy)
# teacher["city"] = "Gdańsk"
# print(teacher)

# Cały klucz usuwamy tak samo jak w przypadku listy
# del teacher["last_name"]
# print(teacher)

# Nie możemy odczytać nieistniejącego klucza
# print(teacher["car"])

# Metody słownika - wyciągnięcie elementu po kluczu
# age = teacher.pop("age")
# print(age)
# print(teacher)

# Metody keys oraz values zwracają obiekty specjalnych typów
# Reprezentujące klucze oraz wartości w słowniku
# print(teacher.keys())
# print(teacher.values())

# Za pomocą funkcji list() możemy zamienić te typy na listę kluczy i wartości
# keys = list(teacher.keys())
# values = list(teacher.values())
# print(keys)
# print(values)

# Funkcja len na słowniku zwraca nam liczbę elementów (kluczy) w słowniku
# print(len(teacher))
