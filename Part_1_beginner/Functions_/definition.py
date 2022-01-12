
# Obieranie ziemniaków - definicja funkcji
def peel_the_potatoes():
    expected_potatoes = int(input("Ile ziemniaków chcesz na obiad? "))
    potatoes = []
    while len(potatoes) < expected_potatoes:
        print("Obieram ziemniaka...")
        print("I wrzucam go do garnka :)")
        potatoes.append("Ziemniak")
    print(potatoes)

############################################################################

# Obieranie ziemniaków - wywołanie funkcji
peel_the_potatoes()
peel_the_potatoes()
peel_the_potatoes() 


def make_soup():
    print("Jest zupa!")


peel_the_potatoes()
make_soup()

