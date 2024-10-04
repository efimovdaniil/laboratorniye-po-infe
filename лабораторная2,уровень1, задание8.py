#Вычислить значение функции y при заданном значении
#арумента x по формуле y=0, если |x|>1, или  y=x**2-1, если |x|<=1
from random import randint, seed
seed(9)

x1 = randint(1,10)
x2 = randint(1,13)
print(x1,x2)

x = float(input("Введите значение x: "))
if abs(x) > 1:
    y = 0
elif abs(x) <= 1:
    y = x**2-1
print("Значение:",y)