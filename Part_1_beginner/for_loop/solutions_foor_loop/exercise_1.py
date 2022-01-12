
# Poproś użytkownika o wprowadzenie ocen które uzyskał/uzyskała.
# Wykorzystaj pęle while aby pytać o kolejne oceny i zakończyć wprowadzanie
# odpowiednim znakiem (np. X). Następnie stosując pętle for oblicz średnią z podanych ocen.

grades = []
grade_input = input("Podaj kolejną ocenę albo zakończ wpisując 'X': ")
while grade_input != 'X':
    grade = int(grade_input)
    grades.append(grade)
    grade_input = input("Podaj kolejną ocenę albo zakończ wpisując 'X': ")

grades_sum = 0
for grade in grades:
    grades_sum += grade

# grades_sum = sum(grades)

average = grades_sum / len(grades)
print(f"Twoja średnia wynosi: {average:.2f}")


