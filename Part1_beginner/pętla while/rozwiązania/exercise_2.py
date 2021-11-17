
# Wczytaj numer telefonu użytkownika i rozdziel go myślnikami (format XXX-XXX-XXX...)

phone_number = input("Podaj numer telefonu: ")
phone_number = phone_number.replace("-", "")
formatted_phone_number = ""
digit_index = 0
while digit_index < len(phone_number):
    if digit_index % 3 == 0 and digit_index != 0:
        formatted_phone_number += "-"
    formatted_phone_number += phone_number[digit_index]
    digit_index += 1

print(f"Twój numer telefonu to: {formatted_phone_number}")
