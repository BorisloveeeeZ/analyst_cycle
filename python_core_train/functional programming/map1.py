# Создайте функцию map, которая добавит к каждой комнате в списке rooms элемент с именем square содержащий её площадь.

rooms = [
    {"name": "кухня", "length": 6, "width": 4},
    {"name": "комната 1", "length": 5.5, "width": 4.5},
    {"name": "комната 2", "length": 5, "width": 4},
    {"name": "комната 3", "length": 7, "width": 6.3},
]

def sq(room):
    room['square'] = room['length'] * room['width']
    return room

result = map(sq, rooms)
print(*result)