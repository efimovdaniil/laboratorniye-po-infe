from random import randint, seed
seed(9)
x1 = randint(1,15)
x2 = randint(1,20)
x3 = randint(1,14)
print(x1,x2,x3)

# подсчитать количество отрицательных элементов заданного одномерного массива размером 6

mass = []
for i in range(6):
    mass.append(int(input("Введите элемент массива: ")))
print("Исходный массив:", mass)

j = 0
n = 0
for i in range(6):
    if mass[n] < 0:
        j+=1
    n+=1
print("Кол-во отрицательных элементов массива: ",j)