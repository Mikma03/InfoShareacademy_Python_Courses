
print("Cześć! Jestem Python i policzę prędkość Twojego biegu :)")
distance_input = input("Ile kilometrów przebiegłeś/przebiegłaś? ")
time_input = input("Ile zajęło Ci to czasu (godzin)? ")

distance = int(distance_input)
time = int(time_input)
speed = distance / time

print("Biegasz z prędkością średnią:", speed, "km/h!")

