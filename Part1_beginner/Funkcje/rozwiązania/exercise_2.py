

# Napisz funkcję liczącą prędkość średnią na podstawie zadanego dystansu i czasu.
# Następnie wykorzystaj ją implementując program, który wyznaczy średnią prędkość biegu,
# średnią prędkość jazdy na rowerze i średnią prędkość jazdy autem.

def avg_speed(distance, time):
    return distance / time


# running_distance = float(input("Ile km przebiegłeś/przebiegłaś? "))
# running_time = float(input("Ile godzin Ci to zajęło? "))
# bike_ride_distance = float(input("Ile km przejechałeś/przejechałaś na rowerze? "))
# bike_ride_time = float(input("Ile godzin Ci to zajęło? "))
# car_drive_distance = float(input("Ile km przejechałeś/przejechałaś autem? "))
# car_drive_time_time = float(input("Ile godzin Ci to zajęło? "))
#
# print(f"Twoja średnia prędkość biegu to {avg_speed(running_distance, running_time)}km/h")
# print(f"Twoja średnia prędkość jazdy rowerem to {avg_speed(bike_ride_distance, bike_ride_time)}km/h")
# print(f"Twoja średnia prędkość jazdy autem to {avg_speed(car_drive_distance, car_drive_time_time)}km/h")


def run_avg_speed_calculator(vehicle_name):
    distance = float(input(f"Ile km pokonałeś/pokonałaś za pomocą {vehicle_name}? "))
    time = float(input("Ile godzin Ci to zajęło? "))
    average_speed = avg_speed(distance, time)
    print(f"Twoja średnia prędkość przemieszczania się za pomocą {vehicle_name} to {average_speed}km/h")

run_avg_speed_calculator("biegu")
run_avg_speed_calculator("roweru")
run_avg_speed_calculator("samochodu")
