
# Poszukiwanie elementu w zbiorze
expenditures = [120, 300, 250.45, 1300, 50, 75]

for expenditure in expenditures:
    print(expenditure)
    if expenditure > 1000:
        print("Drogi wydatek znaleziony!")
        break

############################################################

# Pętla for posiada również opcjonalną część "else"
for expenditure in expenditures:
    if expenditure > 1000:
        print("Drogi wydatek znaleziony!")
        break
else:
    print("Nie znaleziono nic super drogiego")

############################################################

# Break do przerywania wprowadzania informacji od użytkownika
grades = []
while True:
    grade_input = input("Podaj kolejną ocenę albo zakończ wpisując 'X': ")
    if grade_input == "X":
        break
    grade = int(grade_input)
    grades.append(grade)

grades_sum = sum(grades)
average = grades_sum / len(grades)
print(f"Twoja średnia wynosi: {average:.2f}")

############################################################

# Również pętla while ma opcjonalnego else'a
grades = []
while len(grades) < 5:
    grade_input = input("Podaj kolejną ocenę albo zakończ wpisując 'X': ")
    if grade_input == "X":
        break
    grade = int(grade_input)
    grades.append(grade)
else:
    print("Wystarczy już tych ocen")

grades_sum = sum(grades)
average = grades_sum / len(grades)
print(f"Twoja średnia wynosi: {average:.2f}")
