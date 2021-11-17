
# Wypisujemy kod pocztowy - znak po znaku
# post_code = input("Jaki jest Twój kod pocztowy? ")
# letter_index = 0
# while letter_index < len(post_code):
#     print(f"[{letter_index}] -> {post_code[letter_index]}")
#     letter_index += 1


# Zamieniamy kod pocztowy by zawsze był zgodny z formatem XX-XX-XX-XX...
post_code = input("Jaki jest Twój kod pocztowy? ")
post_code = post_code.replace("-", "")
formatted_post_code = ""
letter_index = 0
while letter_index < len(post_code):
    if letter_index % 2 == 0 and letter_index != 0:
        formatted_post_code += "-"
    formatted_post_code += post_code[letter_index]
    letter_index += 1
print(formatted_post_code)
