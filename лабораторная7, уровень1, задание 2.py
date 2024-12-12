from random import randint, seed
seed(9)
x1 = randint(1,3)
x2 = randint(1,28)
x3 = randint(1,7)
print(x1,x2,x3)

#Два треугольника заданы длинами своих сторон a, b и c. Определить треугольник с большей площадью,
# вычисляя площади треугольников по формуле Герона.

import math


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        s = (self.a + self.b + self.c) / 2
        area = math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
        return area


def compare_triangles(triangle1, triangle2):
    area1 = triangle1.area()
    area2 = triangle2.area()

    if area1 > area2:
        return "Первый треугольник имеет большую площадь."
    elif area1 < area2:
        return "Второй треугольник имеет большую площадь."
    else:
        return "Оба треугольника имеют равную площадь."


def input_triangle_sides():
    while True:
        try:
            a = float(input("Введите длину стороны a: "))
            b = float(input("Введите длину стороны b: "))
            c = float(input("Введите длину стороны c: "))
            if a + b > c and a + c > b and b + c > a:
                return a, b, c
            else:
                print("Ошибка: введенные длины не могут образовать треугольник. Попробуйте снова.")
        except ValueError:
            print("Ошибка: введите корректные числовые значения.")


print("Введите стороны первого треугольника:")
a1, b1, c1 = input_triangle_sides()
triangle1 = Triangle(a1, b1, c1)

print("Введите стороны второго треугольника:")
a2, b2, c2 = input_triangle_sides()
triangle2 = Triangle(a2, b2, c2)

result = compare_triangles(triangle1, triangle2)
print(result)
