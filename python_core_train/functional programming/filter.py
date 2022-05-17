# Функция фильтр принимает на вход критерий(другую функцию, которая обрабытвает элементы)
#   Сайт предназначен для мужчин от 20 до 30 лет включительно.
# Отфильтруйте список people, чтобы в нем осталась только целевая аудитория сайта.



people = [
    {"sex": "m", "age": 12},
    {"sex": "w", "age": 12},
    {"sex": "m", "age": 15},
    {"sex": "m", "age": 20},
    {"sex": "m", "age": 13},
    {"sex": "m", "age": 27},
    {"sex": "w", "age": 31},
    {"sex": "m", "age": 17},
    {"sex": "w", "age": 17},
    {"sex": "m", "age": 12},
    {"sex": "m", "age": 42},
    {"sex": "w", "age": 25}
]

people_m = []

def is_men(x):
    if x['sex'] == 'm' and x['age'] in range(20, 30):
        return x

for each in people:
    if is_men(each):
        people_m.append(each)

# Аналог циклу for с использованием функции fliter
my_people = filter(is_men, people)
print(*my_people, *people_m)
