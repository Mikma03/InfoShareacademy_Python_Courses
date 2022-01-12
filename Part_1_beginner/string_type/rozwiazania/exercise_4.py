# Wyobraź sobie, że przetwarzasz dane dotyczące samochodów.
# Numery tablic rejestracyjnych zostały zapisane jednak w niespójny sposób:
# Stwórz zmienne jak powyżej i zmodyfikuj ich wartość,
# tak aby wszystkie były w formacie takim jak Honda (wielkie litery i bez przerwy ciąg cyfr).
# Wypisz wszystkie wyniki.

ford = "ab100100"
audi = "EEE 123123"
citroen = "Zk-300300"
honda = "AB210210"

ford = ford.upper()
audi = audi.upper()
audi = audi.replace(" ", "")
audi = audi.upper().replace(" ", "")
citroen = citroen.upper().replace("-", "")

print(f"Ford: {ford}")
print(f"Audi: {audi}")
print(f"Citroen: {citroen}")
print(f"Honda: {honda}")
