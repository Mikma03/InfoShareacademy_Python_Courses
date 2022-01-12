
# Wypisujemy kod pocztowy - znak po znaku wraz z informacją o kolejności
post_code = input("Jaki jest Twój kod pocztowy? ")
for index, letter in enumerate(post_code):
    print(f"[{index}] -> {letter}")

############################################################

# Wypisywanie co drugiego sportu
favourite_sports = ["bieganie", "pływanie", "jazda na rowerze", "triathlon"]
for index, sport in enumerate(favourite_sports):
    if index % 2 == 0:
        print(sport)

############################################################

# Zamieniamy kod pocztowy by zawsze był zgodny z formatem XX-XX-XX-XX...
post_code = input("Jaki jest Twój kod pocztowy? ")
post_code = post_code.replace("-", "")
formatted_post_code = ""
for index, letter in enumerate(post_code):
    if index % 2 == 0 and index != 0:
        formatted_post_code += "-"
    formatted_post_code += letter
print(formatted_post_code)
