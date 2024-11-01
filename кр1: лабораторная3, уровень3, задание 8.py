#упорядочить по убыванию отрицательные элементы массива, оставляя остальные на прежних местах

n = int(input("Введите размерность массива: "))
mass = []
for i in range(n):
    mass.append(int(input("Введите элемент массива: ")))
print("Исходный массив:", mass)

array = [3, -7, 2, -5, 8, -4]

for i in range(len(mass)):
    if mass[i] < 0:
        for j in range(i+1, len(mass)):
            if mass[j] < 0 and mass[j] > mass[i]:
                mass[i], mass[j] = mass[j], mass[i]

print(mass)
