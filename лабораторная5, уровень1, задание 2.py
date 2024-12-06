#Два треугольника заданы длинами своих сторон a, b и c. Определить треугольник с большей площадью,
# вычисляя площади треугольников по формуле Герона.


from random import randint, seed
seed(9)
x1 = randint(1,3)
x2 = randint(1,28)
x3 = randint(1,7)
print(x1,x2,x3)

import math


def heron_area(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area


def is_triangle(a, b, c):
    return (a + b > c) and (a + c > b) and (b + c > a)


def compare_triangles(a1, b1, c1, a2, b2, c2):
    if not is_triangle(a1, b1, c1):
        return "Первый треугольник не существует."

    if not is_triangle(a2, b2, c2):
        return "Второй треугольник не существует."

    area1 = heron_area(a1, b1, c1)
    area2 = heron_area(a2, b2, c2)

    if area1 > area2:
        return "Первый треугольник имеет большую площадь:", area1
    elif area1 < area2:
        return "Второй треугольник имеет большую площадь:", area2
    else:
        return "Оба треугольника имеют равную площадь:", area1

print("Введите стороны первого треугольника:")
a1 = float(input("Сторона a1: "))
b1 = float(input("Сторона b1: "))
c1 = float(input("Сторона c1: "))

print("Введите стороны второго треугольника:")
a2 = float(input("Сторона a2: "))
b2 = float(input("Сторона b2: "))
c2 = float(input("Сторона c2: "))

result = compare_triangles(a1, b1, c1, a2, b2, c2)
print(result)
