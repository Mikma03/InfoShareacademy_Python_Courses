
# Python przeszukuje zakresy w kolejności: Local -> Enclosing -> Global -> Built in
# Jeżeli nie znajdzie definicji symbolu w żadnym z zakresów - mamy błąd

# Zmienna nie jest dostępna zanim nie zostanie zdefiniowana
print(value)
value = 5
print(value)

#########################################################

# Zmienna musi zostać zdefiniowana zanim wystąpi pierwsze odwołanie do funkcji
# Liczy się kolejność wykonania - nie kolejność w skrypcie
def print_global_name():
    print(name)

print_global_name()
name = "Mikołaj"
print_global_name()

#########################################################

# Zmienna zdefiniowana wewnątrz funkcji
def failed_modify_global_name():
    name = "Kuba"
    print(f"Wewnątrz funkcji: {name}")

name = "Mikołaj"
print(f"Przed funkcją: {name}")
failed_modify_global_name()
print(f"Po funkcji: {name}")


def success_modify_global_name():
    global name
    name = "Kuba"
    print(f"Wewnątrz funkcji: {name}")

name = "Mikołaj"
print(f"Przed funkcją: {name}")
success_modify_global_name()
print(f"Po funkcji: {name}")


PI_NUMBER = 3.141
def circle_area(radius):
    return PI_NUMBER * radius * radius

print(circle_area(radius=30))
