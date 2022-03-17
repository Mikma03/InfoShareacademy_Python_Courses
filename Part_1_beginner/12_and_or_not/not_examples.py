
income = float(input("Jaki jest miesięczny przychód Twojej firmy? "))
number_of_employees = int(input("Ilu pracowników zatrudniasz? "))
support_answer = input("Czy Twoja firma otrzymała już jakieś wsparcie? (T/N) ")

if support_answer == "T":
    support_used = True
else:
    support_used = False

if not support_used and (income < 15500 or number_of_employees >= 3):
    print("Możesz otrzymać dotacje")
else:
    print("Niestety nie otrzymasz dotacji")



# if not 3 < 2:
#     print("3 nie jest mniejsze od 2")
#
#
income = 4000
expenditures = 2000
age = 30

# if age < 18 or income < expenditures:
#     print("Nie możesz wziąć kredytu")
# else:
#     print("Możesz wziąć kredyt")

if not (age < 18 or income < expenditures):
    print("Możesz wziąć kredyt")
else:
    print("Nie możesz wziąć kredytu")

