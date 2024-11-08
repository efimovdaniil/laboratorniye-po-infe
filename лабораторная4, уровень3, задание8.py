#В матрице 7*5 переставить строки таким образом, чтобы количества положительных элементов в строках следовали в порядке убывания.

import random

strings = 5
columns = 7
A = [[random.randint(-100,100) for i in range(columns)] for i in range(strings)]
for i in A:
   print(i)


positive_counts = []
for row in A:
    count = 0
    for num in row:
        if num > 0:
            count += 1
    positive_counts.append(count)
sorted_A = []
while positive_counts:
    max_count = max(positive_counts)
    max_index = positive_counts.index(max_count)
    sorted_A.append(A[max_index])
    positive_counts.pop(max_index)
    A.pop(max_index)
print("\nМатрица после сортировки по количеству положительных элементов:")
for i in sorted_A:
    print(i)