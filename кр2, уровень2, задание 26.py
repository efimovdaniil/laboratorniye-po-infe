#В двух заданных матрицах одинакового размером поменять строки, содержащие максимальное количество отрицательных эле-ментов.
#Нахождение количества отрицательных элементов заданной строки матрицы осуществлять в методе.
#Определение номера стро-ки, содержащей максимальное количество отрицательных элементов, осуществлять в методе.
import random

def generate_matrix(rows, cols):
    return [[random.randint(-10, 10) for _ in range(cols)] for _ in range(rows)]

def count_negative_elements(row):
    return sum(1 for x in row if x < 0)

def find_row_with_max_negatives(matrix):
    max_negatives = -1
    row_index = -1
    for i, row in enumerate(matrix):
        negatives_count = count_negative_elements(row)
        if negatives_count > max_negatives:
            max_negatives = negatives_count
            row_index = i
    return row_index

def swap_rows(matrix1, matrix2, row_index1, row_index2):

    matrix1[row_index1], matrix2[row_index2] = matrix2[row_index2], matrix1[row_index1]

def print_matrix(matrix):
    for row in matrix:
        print(row)

if __name__ == "__main__":
    rows, cols = 4, 5
    matrix1 = generate_matrix(rows, cols)
    matrix2 = generate_matrix(rows, cols)

    print("Матрица 1:")
    print_matrix(matrix1)
    print("\nМатрица 2:")
    print_matrix(matrix2)

    row_index1 = find_row_with_max_negatives(matrix1)
    row_index2 = find_row_with_max_negatives(matrix2)

    print(f"\nСтрока с максимальным количеством отрицательных элементов в матрице 1: {row_index1}")
    print(f"\nСтрока с максимальным количеством отрицательных элементов в матрице 2: {row_index2}")

    swap_rows(matrix1, matrix2, row_index1, row_index2)

    print("\nМатрица 1 после замены:")
    print_matrix(matrix1)
    print("\nМатрица 2 после замены:")
    print_matrix(matrix2)
