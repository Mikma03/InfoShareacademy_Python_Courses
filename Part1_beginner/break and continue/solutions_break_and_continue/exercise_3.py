
# Utwórz listę zawierającą różne liczby i skorzystaj z instrukcji continue aby wypisać tylko nieparzyste.
numbers = [1, 3, 4, 2, 3, 4, 56, 234, 2, 5231, 54, 62, 523, 451, 34]

for number in numbers:
    if number % 2 == 0:
        continue
    print(number)
