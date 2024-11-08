#Дана матрица А размером 5х7. Для каждой строки сравнить элементы,
#расположенные непосредственно перед и после максимального
#элемента этой строки, и меньший из них увеличить в 2 раза.
#Если максимальный элемент является первым или последним в строке,
#то увеличить в 2 раза только один соседний элемент.



import random

strings = 5
columns = 7
A = [[random.randint(0,100) for i in range(columns)] for i in range(strings)]
for i in A:
   print(i)

for i in range(len(A)):
    max_value = max(A[i])
    max_index = A[i].index(max_value)
    if max_index > 0 and max_index < len(A[i]) - 1:
        left_neighbor = A[i][max_index - 1]
        right_neighbor = A[i][max_index + 1]
        if left_neighbor < right_neighbor:
            A[i][max_index - 1] *= 2
        else:
            A[i][max_index + 1] *= 2
    elif max_index == 0:
        A[i][max_index + 1] *= 2
    elif max_index == len(A[i]) - 1:
        A[i][max_index - 1] *= 2
print("\nМатрица после обработки:")
for i in A:
    print(i)