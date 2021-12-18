
# Napisz funkcję, która podaną liczbę zamieni na zakres.
# Domyślnie przyjmujemy zakres jako +/- 10% podanej wartości.

def value_with_tolerance(value, tolerance_percentage=10):
    tolerance_value = tolerance_percentage * value / 100
    return value - tolerance_value, value + tolerance_value


print(value_with_tolerance(value=100))
print(value_with_tolerance(value=100, tolerance_percentage=40))
