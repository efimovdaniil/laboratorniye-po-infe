from random import randint, seed
seed(1009)
import random
task1 = random.randint(1,33)
task2 = random.randint(1,9)
task3 = random.randint(1,14)
print(task1,task2,task3)

#В матрице 6*7 удалить столбец и строку, на пересечении которых находится максимальный элемент матрицы


strings = 6
columns = 7
A = [[random.randint(0,99) for i in range(columns)] for i in range(strings)]
for i in A:
   print(i)


max_value = A[0][0]
max_row = 0
max_col = 0
for i in range(len(A)):
    for j in range(len(A[i])):
        if A[i][j] > max_value:
            max_value = A[i][j]
            max_row = i
            max_col = j

new_A = []
for i in range(len(A)):
    if i != max_row:
        new_row = []
        for j in range(len(A[i])):
            if j != max_col:
                new_row.append(A[i][j])
        new_A.append(new_row)
print("\nМатрица после удаления строки и столбца с максимальным элементом:")
for i in new_A:
    print(i)