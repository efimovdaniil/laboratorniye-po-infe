#В двух заданных матрицах удалить все столбцы, не содержащих нулевых элементов. Удаление столбца в матрице оформить в виде функции.



def remove_nonzero_columns(matrix):
    transposed_matrix = list(zip(*matrix))
    filtered_columns = [col for col in transposed_matrix if 0 in col]
    filtered_matrix = [list(row) for row in zip(*filtered_columns)]

    return filtered_matrix


def create_matrix(rows, cols):
    matrix = []
    print(f"Введите элементы матрицы {rows}x{cols}:")
    for i in range(rows):
        row = list(map(float, input(f"Строка {i + 1}: ").split()))
        if len(row) != cols:
            print(f"Ошибка: ожидается {cols} элементов, но введено {len(row)}. Попробуйте снова.")
            return create_matrix(rows, cols)
        matrix.append(row)
    return matrix


rows1 = int(input("Введите количество строк для первой матрицы: "))
cols1 = int(input("Введите количество столбцов для первой матрицы: "))
matrix1 = create_matrix(rows1, cols1)

rows2 = int(input("Введите количество строк для второй матрицы: "))
cols2 = int(input("Введите количество столбцов для второй матрицы: "))
matrix2 = create_matrix(rows2, cols2)

filtered_matrix1 = remove_nonzero_columns(matrix1)
filtered_matrix2 = remove_nonzero_columns(matrix2)

print("\nИсходная матрица 1:")
for row in matrix1:
    print(row)
print("Матрица 1 после удаления столбцов:")
for row in filtered_matrix1:
    print(row)

print("\nИсходная матрица 2:")
for row in matrix2:
    print(row)
print("Матрица 2 после удаления столбцов:")
for row in filtered_matrix2:
    print(row)
