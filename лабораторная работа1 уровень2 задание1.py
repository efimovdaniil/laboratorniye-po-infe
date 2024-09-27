
#Уровень 2 задание 1.
#Вычислите сумму = cos x + (cos 2x)/22 + ... + (cos nx)/n²+ ... .
#Суммирование прекратить, когда очередной член суммы по модулю будет меньше в = 0,0001


import math
s = 0
n = 1
E = 0.0001
x = int(input("Введите x"))
d = math.fabs(math.cos(n*x)/n**2)
while d >= E:
    d = math.fabs(math.cos(n*x)/n**2)
    s += d
    n += 1
print ("Ответ:", round(s, 3))