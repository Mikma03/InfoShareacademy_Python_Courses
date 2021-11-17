
walk_distance_input = input("Ile kilometrów przeszedłeś/przeszłaś dziś? ")
walk_distance = int(walk_distance_input)
around_earth_distance = 40075
days_around_earth = around_earth_distance / walk_distance
weeks_around_earth = days_around_earth / 7

print("W takim tempie okrążenie Ziemi zajmie Ci", weeks_around_earth, "tygodni")

