# Напишите класс Vector, который на вход будет принимать список координат (x1,…,xn ). Положите все координаты вектора в список self.coords.
# Добейтесь того, чтобы объекты класса Vector можно было складывать через оператор + и получать на выходе тоже объект этого же класса. Например
# Будет работать
# Vector([1, 2, 3]) + Vector((2, 3, 4)) # даст Vector([3, 5, 7])

# НЕ будет работать
#Vector([1, 2]) + Vector([1, 2, 3])  # нельзя складывать векторы разной длины

# Добавьте методу красивый вывод при передаче его в print(...). Пример: print(Vector([1, 2, 3])  Напечатает: "[1, 2, 3]" без кавычек

#Продолжаем улучшать вектор. 
# Добавьте в класс возможность умножать вектор на вектор и вектор на число.


#Добавьте в класс возможности сравнивать два вектора между собой и считать abs (это длина вектора, в Евклидовой метрике).

#abs(Vector([-12, 5]))  # Должно быть 13

# Vector([1, 3, 5]) == Vector([1])  # False
# Vector([1, 3, 5]) == Vector([-1, 3, 5])  # False
# Vector([1, 3, 5]) == Vector([1, 3, 5])  # True
# По итогу мы получим вектора, которые можно складывать, умножать, печатать, считать длину и сравнивать на равенство друг с другом.


class Vector:

    def __init__(self, coords: list) -> list:
        self.coords = coords

    def __add__(self, other: list):
        length_1 = len(other.coords)
        length_2 = len(self.coords)
        if len(other.coords) != len(self.coords):
            raise ValueError(f'left and right lengths differ: {length_2} != {length_1}')
        else:
            return Vector([self.coords[i] + other.coords[i] for i in range(length_1)])

    def __str__(self):
        return f'{[self.coords[i] for i in range(len(self.coords))]}'

    def __mul__(self, other):

        if isinstance(other,int):
            return Vector([self.coords[element] * other for element in range(len(self.coords))])
        else:
            length_1, length_2 = len(other.coords), len(self.coords)
            if length_1 != length_2:
                raise ValueError(f'left and right lengths differ: {length_2} != {length_1}')
            else:
                list11 = [self.coords[i] * other.coords[i] for i in range(length_1)]
                return sum(list11)

    def __abs__(self):
        return sum([self.coords[i]**2 for i in range(len(self.coords))])**0.5

    def __eq__(self, other):
        return self.coords == other.coords