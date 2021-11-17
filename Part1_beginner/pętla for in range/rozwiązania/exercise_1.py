
# Poproś użytkownika o podanie numeru telefonu.
# Następnie wypisz informacje ile razy występuje w nim każda cyfra.
phone_number = input("Podaj numer telefonu: ")
for digit in range(10):
    digit_times_in_number = phone_number.count(str(digit))
    print(f"Cyfra {digit} występuje w Twoim numerze: {digit_times_in_number} razy")
