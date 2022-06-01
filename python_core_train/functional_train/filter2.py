#Напишите функцию normalize_phone, которая принимает номер телефона в произвольной форме,
# а затем возвращает строку, которая содержит только цифры этого номера.
#Используйте возможности функционального программирования.
from functools import reduce

def normalize_phone(x):
    result = reduce(lambda a,b: a + b, filter(lambda y: y in '0123456789', x))
    return result
