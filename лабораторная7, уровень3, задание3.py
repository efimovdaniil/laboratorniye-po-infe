#Вычислить сумму элементов с нечетными индексами заданного массива, в котором предварительно производится попарная перестановка соседних элементов,
# начиная либо с первого (если значение первого элемента больше среднего арифметического элементов массива), либо с последнего элемента (в противном случае).
#Для нахождения суммы элементов с нечетными индексами использовать метод, для перестановки элементов массива - делегат.

class ArrayProcessor:
    def __init__(self, data):
        self.data = data

    def swap_elements(self, start_index):
        for i in range(start_index, len(self.data) - 1, 2):
            self.data[i], self.data[i + 1] = self.data[i + 1], self.data[i]

    def calculate_sum_of_odd_indices(self):
        return sum(self.data[i] for i in range(1, len(self.data), 2))

    def process_array(self):
        average = sum(self.data) / len(self.data)
        first_element = self.data[0]

        if first_element > average:
            self.swap_elements(0)
        else:
            self.swap_elements(len(self.data) - 2)

def input_array():
    while True:
        try:
            array_input = list(map(int, input("Введите элементы массива через пробел: ").split()))
            return array_input
        except ValueError:
            print("Ошибка: введите корректные числовые значения.")

print("Введите данные для массива:")
array_data = input_array()
processor = ArrayProcessor(array_data)

processor.process_array()

result_sum = processor.calculate_sum_of_odd_indices()

print(f"Обработанный массив: {processor.data}")
print(f"Сумма элементов с нечетными индексами: {result_sum}")
