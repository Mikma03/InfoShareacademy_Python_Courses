
# Napisz funkcję, dodającą kolejne osoby do listy uczęszczających na zajęcia.
# Funkcja przyjmuje napis, który zawiera imiona rozdzielone przecinkiem
# oraz listę już zapisanych osób, która domyślnie jest pusta.
def add_people_to_classes(names_str, participants=None):
    if participants is None:
        participants = []
    names = names_str.split(',')
    for name in names:
        participants.append(name)
    # participants += names
    return participants

attendees_names = "Ola,Bob,Ala,Kuba"
monday_course_participants = add_people_to_classes(attendees_names)
print(monday_course_participants)
attendees_names = "Paweł,Dominika"
monday_course_participants = add_people_to_classes(attendees_names, participants=monday_course_participants)
print(monday_course_participants)


attendees_names = "Ania,Krzysztof"
friday_course_participants = add_people_to_classes(attendees_names)
print(friday_course_participants)
