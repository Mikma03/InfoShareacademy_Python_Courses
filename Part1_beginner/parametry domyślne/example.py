
# Wartość domyślna

def best_grades(grades, best_grades_number=1):
    grades.sort(reverse=True)
    if best_grades_number < len(grades):
        return grades[:best_grades_number]
    print("Nie można zwrócić więcej ocen niż jest na liście. Zostaną zwrócone wszystkie...")
    return grades


math_grades = [1, 3, 4, 1, 2, 5, 4]
print(best_grades(math_grades))
print(best_grades(math_grades, 4))
print(best_grades(math_grades, best_grades_number=4))


# Również funkcja print ma domyślne argumenty
# print("Domyślny", "separator")
# print("Własny", "separator", sep='---')


# Wartości domyślne muszą być po wartościach nie domyślnych
# def best_grades(best_grades_number=1, grades):
#     grades.sort(reverse=True)
#     if best_grades_number < len(grades):
#         return grades[:best_grades_number]
#     print("Nie można zwrócić więcej ocen niż jest na liście. Zostaną zwrócone wszystkie...")
#     return grades


# UWAGA! Jeżeli jako domyślnego argumentu chcemy użyć listy lub słownika
# Należy to zrobić w ten sposób
def write_final_grade(subject_grades, final_grades=None):
    if final_grades is None:
        final_grades = []
    grades_avg = sum(subject_grades) / len(subject_grades)
    final_grades.append(int(grades_avg))
    return final_grades


# # UWAGA! TAK JEST ZLE!
# def write_final_grade(subject_grades, final_grades=[]):
#     grades_avg = sum(subject_grades) / len(subject_grades)
#     final_grades.append(int(grades_avg))
#     return final_grades


# john_math_grades = [3, 4, 5, 2, 5]
# john_physics_grades = [4, 4, 4, 4, 4]
# john_final_grades = write_final_grade(subject_grades=john_math_grades)
# john_final_grades = write_final_grade(subject_grades=john_physics_grades, final_grades=john_final_grades)
# print(f"Oceny John'a: {john_final_grades}")
#
# bob_math_grades = [5, 5, 5]
# bob_physics_grades = [3, 3, 3, 4, 4]
# bob_final_grades = write_final_grade(subject_grades=bob_math_grades)
# bob_final_grades = write_final_grade(subject_grades=bob_physics_grades, final_grades=bob_final_grades)
# print(f"Oceny Bob'a: {bob_final_grades}")
# print(f"Oceny John'a: {john_final_grades}")
#

# UWAGA! Jeżeli jako domyślnego argumentu chcemy użyć listy lub słownika
# Należy to zrobić w ten sposób
def do_something_with_default_dict(something=None):
    if something is None:
        something = {}
    print("Tutaj dalsza implementacja...")
