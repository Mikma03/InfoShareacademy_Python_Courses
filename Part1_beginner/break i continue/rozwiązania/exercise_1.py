
# Zmodyfikuj rozwiązanie zadania z promocją do następnej klasy
# (zadanie 3 z lekcji o if/else z modułu 4).
# Wczytaj oceny do listy, jeżeli jest jakakolwiek jedynka to klasę trzeba powtórzyć,
# w przeciwnym razie należą się gratulacje :)


subjects = ["matematyka", "fizyka", "język polski", "języka angielski", "historia"]
grades = []
for subject in subjects:
    grade = int(input(f"Jaka jest Twoja ocena końcowa z przedmiotu {subject}? "))
    grades.append(grade)

for grade in grades:
    if grade == 1:
        print("Niestety...")
        break
else:
    print("Gratuluję! Zdałeś/zdałaś do następnej klasy :)")
