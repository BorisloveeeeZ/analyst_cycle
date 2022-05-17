#ВОДИТЕЛИ ТАКСИ
#В такси «Везет» есть два условия к водителям при приеме на работу:
   #1. Автомобиль кандидата должен быть выпущен не ранее 2008 года (машины 2008 года годятся).
   #2. Стаж водителя должен быть не менее трех лет.


drivers = [
    {"name": "Семен", "car_year": 2003, "experience": 2},
    {"name": "Степан", "car_year": 2013, "experience": 3},
    {"name": "Ашот", "car_year": 2007, "experience": 5},
    {"name": "Дмитрий", "car_year": 2003, "experience": 0},
    {"name": "Василий", "car_year": 2016, "experience": 1},
    {"name": "Антон", "car_year": 2008, "experience": 7},
    {"name": "Денис", "car_year": 2007, "experience": 5},
    {"name": "Ахмед", "car_year": 2006, "experience": 3},
    {"name": "Виталий", "car_year": 2003, "experience": 2}
]

taxi_drivers = filter(lambda x: x['car_year'] >= 2008 and x['experience'] >= 3, drivers)
print(*taxi_drivers)