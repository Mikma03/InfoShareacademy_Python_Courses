

# Zmodyfikuj rozwiązanie zadania z prędkością średnią z poprzedniej lekcji
# wywołując funkcję z zastosowaniem argumentów nazwanych

def avg_speed(distance, time):
    return distance / time


def run_avg_speed_calculator(vehicle_name):
    distance = float(input(f"Ile km pokonałeś/pokonałaś za pomocą {vehicle_name}? "))
    time = float(input("Ile godzin Ci to zajęło? "))
    average_speed = avg_speed(distance=distance, time=time)
    print(f"Twoja średnia przemieszczania się za pomocą {vehicle_name} to {average_speed}km/h")


run_avg_speed_calculator(vehicle_name="biegu")
run_avg_speed_calculator(vehicle_name="roweru")
run_avg_speed_calculator(vehicle_name="samochodu")
