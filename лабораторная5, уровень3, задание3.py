#Вычислить сумму элементов с нечетными индексами заданного массива, в котором предварительно производится попарная перестановка соседних элементов,
# начиная либо с первого (если значение первого элемента больше среднего арифметического элементов массива), либо с последнего элемента (в противном случае).
#Для нахождения суммы элементов с нечетными индексами использовать метод, для перестановки элементов массива - делегат.


def swap_pairs(arr):
    for i in range(0, len(arr) - 1, 2):
        arr[i], arr[i + 1] = arr[i + 1], arr[i]

def swap_pairs_reverse(arr):
    for i in range(len(arr) - 1, 0, -2):
        arr[i], arr[i - 1] = arr[i - 1], arr[i]

def calculate_sum_of_odd_indices(arr):
    return sum(arr[i] for i in range(1, len(arr), 2))

def main():
    array = list(map(float, input("Введите элементы массива через пробел: ").split()))
    average = sum(array) / len(array)
    print(f"Среднее арифметическое: {average}")
    if array[0] > average:
        swap_function = swap_pairs
    else:
        swap_function = swap_pairs_reverse

    swap_function(array)
    sum_odd_indices = calculate_sum_of_odd_indices(array)

    print("Массив после перестановки:", array)
    print("Сумма элементов с нечетными индексами:", sum_odd_indices)

if __name__ == "__main__":
    main()
