
# Zmienna result została zdefiniowana wewnątrz funkcji i nie mamy do niej dostępu spoza niej

# def avg_speed(distance, time):
#     result = distance / time
#     print("Nic nie zwracam - ha ha!")

# avg_speed(30, 2)
# print(result)

#########################################################

# Zmienna distance została zdefiniowana poza jakąkolwiek funkcją - jest globalna
def avg_speed(time):
    result = distance / time
    return result


distance = 20
time_in_hours = 2
print(avg_speed(time_in_hours))

#########################################################

# Zmienna distance jest zdefiniowana w inne funkcji - jest lokalna i niedostępna spoza tej funkcji
def avg_speed(time):
    result = distance / time
    return result

def calculate_avg_speed():
    distance = 20
    time_in_hours = 2
    print(avg_speed(time_in_hours))

calculate_avg_speed()
print(distance)
