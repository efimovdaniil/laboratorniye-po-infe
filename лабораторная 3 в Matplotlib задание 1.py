"""
Вариант №9
"""

import numpy as np
import matplotlib.pyplot as plt

print("Вы сможете построить график функции: y = a * x**3 - np.sin(b * x)")
a = int(input("Задайте параметр 'a' >> "))
b = int(input("Задайте параметр 'b' >> "))
c = int(input("Задайте параметр 'c' >> "))
n = int(input("Задайте размерность массива >> "))

x = np.linspace(0, n, 100)

y = a + b+x + c*x**3

plt.figure(figsize=(10, 8))
plt.plot(x, y, label=f'y = {a} + {b}*x + {c}*x**3')
plt.title('График функции y = a+bx+cx^3')
plt.xlabel('x')
plt.yticks(rotation = 90)
plt.ylabel('y')
plt.grid(True)
plt.show()