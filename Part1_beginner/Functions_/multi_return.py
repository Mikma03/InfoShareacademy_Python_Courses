
def find_best_grade(grades_by_subject):
    best_subject = None
    best_grade = 0
    for subject, grades in grades_by_subject.items():
        best_grade_from_subject = max(grades)
        if best_grade_from_subject > best_grade:
            best_grade = best_grade_from_subject
            best_subject = subject
    return best_grade, best_subject


grades_data = {
    "Historia": [5, 5, 4, 5],
    "Matematyka": [5, 4, 3, 6],
    "Fizyka": [4, 3, 2, 5]
}
the_best_grade, subject = find_best_grade(grades_data)
print(f"Najlepsza uzyskana ocena to {the_best_grade} z {subject}")

result = find_best_grade(grades_data)
print(result[0])
print(type(result))
