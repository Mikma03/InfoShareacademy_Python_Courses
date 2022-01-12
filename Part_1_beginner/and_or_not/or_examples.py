
income = float(input("Jaki jest miesięczny przychód Twojej firmy? "))
number_of_employees = int(input("Ilu pracowników zatrudniasz? "))

# if income < 15500 or number_of_employees >= 3:
#     print("Możesz otrzymać dotacje")
# else:
#     print("Niestety nie otrzymasz dotacji")

# Operatory and i or można łączyć
if income < 15500 or (number_of_employees >= 3 and income < 30000):
    print("Możesz otrzymać dotacje")
else:
    print("Niestety nie otrzymasz dotacji")
