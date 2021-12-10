# Zapytaj użytkownika o numer telefonu i wypisz go w postaci zanonimizowanej:
# wypisz pierwsze 6 cyfr, pozostałe zastąp myślnikiem

phone_number = input("Jaki jest Twój numer telefonu? ")
phone_number = phone_number.replace("-", "")
public_digits = phone_number[:6]
number_of_private_digits = len(phone_number) - 6
private_digits = "-" * number_of_private_digits
anonymous_number = f"{public_digits}{private_digits}"

print("Zanonimizowany numer:", anonymous_number)
