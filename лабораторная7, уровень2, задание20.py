#В двух заданных матрицах удалить все столбцы, не содержащих нулевых элементов. Удаление столбца в матрице оформить в виде функции.

class Matrix:
    def __init__(self, data):
        self.data = data

    def remove_empty_columns(self):
        new_data = []
        for col in range(len(self.data[0])):
            if any(row[col] == 0 for row in self.data):
                new_data.append([row[col] for row in self.data])

        self.data = list(map(list, zip(*new_data)))

    def display(self):
        for row in self.data:
            print(" ".join(map(str, row)))


def input_matrix():
    while True:
        try:
            rows = int(input("Введите количество строк: "))
            cols = int(input("Введите количество столбцов: "))
            matrix_data = []

            for i in range(rows):
                row = list(map(int, input(f"Введите элементы строки {i + 1} через пробел: ").split()))
                if len(row) != cols:
                    raise ValueError("Количество элементов в строке должно соответствовать количеству столбцов.")
                matrix_data.append(row)

            return matrix_data
        except ValueError as e:
            print(f"Ошибка: {e}. Попробуйте снова.")

print("Введите данные для первой матрицы:")
matrix1_data = input_matrix()
matrix1 = Matrix(matrix1_data)

print("Введите данные для второй матрицы:")
matrix2_data = input_matrix()
matrix2 = Matrix(matrix2_data)

matrix1.remove_empty_columns()
matrix2.remove_empty_columns()

print("\nПервая матрица после удаления столбцов:")
matrix1.display()

print("\nВторая матрица после удаления столбцов:")
matrix2.display()
