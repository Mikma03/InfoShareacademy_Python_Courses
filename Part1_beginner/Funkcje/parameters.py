
def put_a_brick():
    print("-", sep="", end="")


# Funkcja może wołać inną funkcję
# def build_a_wall():
#     wall_length = 10
#     for brick in range(wall_length):
#         put_a_brick()
#     print()
#
# build_a_wall()


# def build_longer_wall():
#     wall_length = 30
#     for brick in range(wall_length):
#         put_a_brick()
#     print()
#
# build_longer_wall()
#
#

# Funkcja może przyjmować parametry - widoczne wewnątrz jako zmienne
def function_with_params(something, something_else):
    print(something)
    print(something_else)
#
#
# function_with_params(1, 4)
# function_with_params("Napis", 4)
# list_example = ["Lista", "z", "elementami"]
# dict_example = {'Klucz': 'Wartość'}
# function_with_params(list_example, dict_example)

# Jeżeli funkcja definiuje parametry, to muszą one zostać przekazane
# function_with_params()
# function_with_params(1)

# Nie można przekazać nadmiarowych argumentów
# function_with_params(1, 2, 3)

def build_a_wall(wall_length):
    for brick in range(wall_length):
        put_a_brick()
    print()
#
#
build_a_wall(20)
build_a_wall(5)
build_a_wall(45)
