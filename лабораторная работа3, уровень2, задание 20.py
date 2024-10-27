#Если первый отрицательный элемент массива расположен до минимального, то найти сумму элементов с четными индексами, иначе - с нечетными

n = int(input("Введите размерность массива: "))
mass = []
for i in range(n):
    mass.append(int(input("Введите элемент массива: ")))
print("Исходный массив:", mass)

g = 0
for x in range(len(mass)):
    if mass[x] < 0:
        if mass.index(mass[x]) < mass.index(min(mass)):
            g = sum(mass[::2])
            print("Будут суммироваться элементы с четными индексами")
            break
        else:
            g = sum(mass[1::2])
            print("Будут суммироваться элементы с нечетными индексами")
            break
    else:
        continue
print("Cумма:", g)
