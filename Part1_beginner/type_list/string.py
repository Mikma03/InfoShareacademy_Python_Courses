
name = "Mikołaj"

# Możemy odwołać się do konkretnego znaku w napisie za pomocą indeksu
# print("Pierwsza litera imienia to:", name[0])
# print("Ostatnia litera imienia to:", name[-1])
# print("Wszystkie litery poza pierwszą:", name[1:])

# To nie zadziała
# name[0] = "N"
# print(name)

# Możemy to zrobić w taki sposób
# name = "N" + name[1:]
# print(name)

# Metoda split na stringu zwraca listę stringów
words = "To jest całe zdanie".split(" ")
print(words)
print("Pierwsze słowo:", words[0])
