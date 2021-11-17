
# Przykłady z if wzbogacone o instrukcję else
# if 7 > 3:
#     print("To oczywiste!")
# else:
#     print("To się nie wydarzy")

# if 10 < 4:
#     print("To się nigdy nie zdarzy")
# else:
#     print("A to się wydarzy zawsze")

# name = input("Jak się nazywasz? ")
# print(f"Miło Cię poznać {name}")
#
# if len(name) >= 7:
#     print(f"{name} to całkiem długie imie!")
# else:
#     print(f"{name} to raczej krótkie imie")
#
age = int(input("Ile masz lat? "))

# if age < 18:
#     print("Jeszcze nie możesz głosować")
# else:
#     print("Możesz już głosować!")
#

if age < 18:
    print("Jeszcze nie możesz głosować")
else:
    print("Możesz już głosować!")
    if age >= 21:
        print("Możesz kandydować na posła")
    if age >= 30:
        print("Możesz kandydować na senatora")
    if age >= 35:
        print("Możesz kandydować na prezydenta")



