
# Zmodyfikuj zadanie, w którym pytasz użytkownika o listę zakupów
# i sprawdź, czy znajdują się na niej chleb albo bułki.

shopping_elements = input("Wprowadź listę zakupów, rozdzielając poszczególne elementy przecinkiem: ")
shopping_list = shopping_elements.split(",")

if "chleb" in shopping_list or "bułki" in shopping_list:
    print("Planujesz kupić pieczywo")
