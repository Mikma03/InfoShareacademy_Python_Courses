
# Instrukcja warunkowa if jest bardzo czytelna
if 7 > 3:
    print("To oczywiste!")

if 10 < 4:
    print("To się nigdy nie zdarzy")
    print("Inne")

# If w połączeniu z dynamicznymi (np. wprowadzanymi przez użytkownika) danymi
name = input("Jak się nazywasz? ")
print(f"Miło Cię poznać {name}")

if len(name) >= 7:
    print(f"{name} to całkiem długie imię!")
if len(name) < 7:
    print(f"{name} to raczej krótkie imię")


age = int(input("Ile masz lat? "))
if age < 18:
    print("Jeszcze nie możesz głosować")
if age >= 18:
    print("Możesz już głosować!")
if age >= 21:
    print("Możesz kandydować na posła")
if age >= 30:
    print("Możesz kandydować na senatora")
if age >= 35:
    print("Możesz kandydować na prezydenta")

# Drobna pomyłka - program nie działa poprawnie!
if age < 18:
    print("Jeszcze nie możesz głosować")
if age >= 8:
    print("Możesz już głosować!")
