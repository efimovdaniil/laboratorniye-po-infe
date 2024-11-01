from random import randint, seed
seed(1009)
import random
task1 = random.randint(1,18)
task2 = random.randint(1,13)
task3 = random.randint(1,14)
print(task1,task2,task3)

#получить таблицу функции y(x)=0.5*x**2-7*x при изменении x от -4 до 4 с шагом 0.5
x = -4
def y(x):
    return 0.5*x**2-7*x
for i in range(17):
    print("x =",x,"\t|   y(x) =",y(x))
    x += 0.5


#второй способ:
for n in range(-8,9,1):
    y = 0.5 * (n / 2) ** 2 - 7 * (n / 2)
    print("x =", n/2, "\t|   y(x) =", y)
