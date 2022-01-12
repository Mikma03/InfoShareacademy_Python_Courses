
# Zmodyfikuj zadanie z poprzedniej lekcji dotyczące formatowania
# numeru telefonu - zastąp pętle while pętlą for (i enumerate)

phone_number = input("Podaj numer telefonu: ")
phone_number = phone_number.replace("-", "")
formatted_phone_number = ""
for index, digit in enumerate(phone_number):
    if index % 3 == 0 and index != 0:
        formatted_phone_number += "-"
    formatted_phone_number += phone_number[index]

print(f"Twój numer telefonu to: {formatted_phone_number}")
