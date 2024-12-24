from random import randint, seed
seed(3109)
x1 = randint(1,33)
x2 = randint(1,28)
x3 = randint(1,6)
print(x1,x2,x3)

#В матрице А размером 5 х 7 поменять местами строку, содержащую максимальный элемент в 3-м столбце, с 4-й строкой.
import random

rows, cols = 5, 7
A = [[random.randint(1, 100) for _ in range(cols)] for _ in range(rows)]

print("Исходная матрица A:")
for row in A:
    print(row)

max_index = 0
max_value = A[0][2]

for i in range(1, rows):
    if A[i][2] > max_value:
        max_value = A[i][2]
        max_index = i

A[max_index], A[3] = A[3], A[max_index]

print("\nМатрица A после замены:")
for row in A:
    print(row)
