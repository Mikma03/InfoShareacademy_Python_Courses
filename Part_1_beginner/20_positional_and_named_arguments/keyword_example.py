
# Taka sama definicja funkcji
def calculate_investment_value(initial_value, percentage, years):
    result = initial_value * (1 + percentage / 100) ** years
    return result

#########################################################

# Inne wywołanie - większa czytelność
final_value = calculate_investment_value(initial_value=1000, percentage=5, years=4)
print(f"Po 4 latach Twoja lokata będzie warta {final_value:.2f}")

#########################################################

# Możemy przekazywać argumenty w dowolnej kolejności - o ile je nazwiemy
final_value = calculate_investment_value(percentage=5, years=4, initial_value=1000)
print(f"Po 4 latach Twoja lokata będzie warta {final_value:.2f}")

#########################################################

# Argumenty nazwane powodują dłuższy zapis
initial = 1000
percentage = 5
years = 4

final_value = calculate_investment_value(initial_value=initial, percentage=percentage, years=years)
print(f"Po {years} latach Twoja lokata będzie warta {final_value:.2f}")

#########################################################

# W jednym wywołaniu możemy łączyć argumenty pozycyjne i nazwane
final_value = calculate_investment_value(initial, percentage=percentage, years=years)
print(final_value)

#########################################################

# Argumenty pozycyjne muszą być podane w odpowiedniej kolejności PRZED nazwanymi!!!!!!!
# final_value = calculate_investment_value(initial_value=initial, percentage, years)
# print(final_value)
