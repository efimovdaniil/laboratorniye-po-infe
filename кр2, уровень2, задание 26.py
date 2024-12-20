#В двух заданных матрицах одинакового размером поменять строки, содержащие максимальное количество отрицательных эле-ментов.
#Нахождение количества отрицательных элементов заданной строки матрицы осуществлять в методе.
#Определение номера стро-ки, содержащей максимальное количество отрицательных элементов, осуществлять в методе.

def count_negative_elements(row):
    return sum(1 for x in row if x < 0)


def find_row_with_max_negatives(matrix):
    max_neg_count = -1
    max_row_index = -1

    for i, row in enumerate(matrix):
        neg_count = count_negative_elements(row)
        if neg_count > max_neg_count:
            max_neg_count = neg_count
            max_row_index = i

    return max_row_index


def swap_rows(matrix1, matrix2, row1_index, row2_index):
    matrix1[row1_index], matrix2[row2_index] = matrix2[row2_index], matrix1[row1_index]


def main():
    rows, cols = 3, 4
    print("Введите значения для первой матрицы (3x4):")
    matrix1 = []
    for i in range(rows):
        row = list(map(int, input(f"Введите 4 целых числа для строки {i + 1}, разделенных пробелом: ").split()))
        while len(row) != cols:
            print(f"Ошибка: необходимо ввести ровно {cols} чисел.")
            row = list(map(int, input(f"Введите 4 целых числа для строки {i + 1}, разделенных пробелом: ").split()))
        matrix1.append(row)

    print("\nВведите значения для второй матрицы (3x4):")
    matrix2 = []
    for i in range(rows):
        row = list(map(int, input(f"Введите 4 целых числа для строки {i + 1}, разделенных пробелом: ").split()))
        while len(row) != cols:
            print(f"Ошибка: необходимо ввести ровно {cols} чисел.")
            row = list(map(int, input(f"Введите 4 целых числа для строки {i + 1}, разделенных пробелом: ").split()))
        matrix2.append(row)

    print("\nПервая матрица:")
    for row in matrix1:
        print(row)

    print("\nВторая матрица:")
    for row in matrix2:
        print(row)

    row1_index = find_row_with_max_negatives(matrix1)
    row2_index = find_row_with_max_negatives(matrix2)
    swap_rows(matrix1, matrix2, row1_index, row2_index)

    # Печатаем измененные матрицы
    print("\nПервая матрица после замены строк:")
    for row in matrix1:
        print(row)

    print("\nВторая матрица после замены строк:")
    for row in matrix2:
        print(row)


if __name__ == "__main__":
    main()
