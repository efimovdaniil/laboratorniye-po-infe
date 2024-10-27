#В массиве A найти максимальное количество следующих подряд упорядоченных по убыванию элементов

n = int(input("Введите размерность массива: "))
mass = []
for i in range(n):
    mass.append(int(input("Введите элемент массива: ")))
print("Исходный массив:", mass)

m = 1
c = 1
for i in range(1, len(mass)):
        if mass[i - 1] > mass[i]:
            c += 1
            m = max(m, c)
        else:
            c = 1


print("Ответ: ",m)