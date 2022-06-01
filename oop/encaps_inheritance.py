# Напишите класс BaseFigure, который имеет поле класса (т.е. на уровне класса) n_dots = None, метод area() "без реализации", метод validate() "без реализации".
#  Сделайте так, чтобы методы "без реализации" выбрасывали исключение NotImplementedError при их вызове и ничего другого не делали.
#  Создайте также конструктор класса, который не принимает дополнительных аргументов и в реализации только лишь вызывает self.validate().
# Унаследуйте от базового класса треугольник и прямоугольник, оба должны иметь ПРОВЕРКУ на валидность, затем унасдеуйте круг, который не осуществляет проверку

class BaseFigure():

    n_dots = None

    def __init__(self):
        return self.validate()

    def area(self):
        raise NotImplementedError

    def validate(self):
        raise NotImplementedError


class Triangle(BaseFigure):

    n_dots = 3

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.p = (self.a + self.b + self.c) * 0.5
        super().__init__()

    def validate(self):
        if self.a > self.b + self.c or self.b > self.a + self.c or self.c > self.b + self.a:
            raise ValueError("triangle inequality does not hold")
        else:
            return self.a, self.b, self.c

    def area(self):
        return (self.p * (self.p - self.a) * (self.p - self.b) * (self.p - self.c)) ** 0.5


class Rectangle(BaseFigure):
    
    n_dots = 4

    def __init__(self, a, b):
        self.a = a
        self.b = b
        super().__init__()

    def validate(self):
        return self.a, self.b

    def area(self):
        return self.a * self.b


class Circle(BaseFigure):

    n_dots = float('inf')

    def __init__(self,r):
        self.r = r
        super().__init__()

    def area(self):
        return 3.14 * (self.r **2)

    def validate(self):
        pass    

