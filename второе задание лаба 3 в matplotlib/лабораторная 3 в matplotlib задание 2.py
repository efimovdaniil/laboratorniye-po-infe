#Вариант 9

import numpy as np
import matplotlib.pyplot as plt

with open('tabl.txt', 'r') as file:
    lines = file.readlines()

X = list(map(float, lines[0].strip().split(':')[1].split(',')))
Y = list(map(float, lines[1].strip().split(':')[1].split(',')))

plt.figure(figsize=(10, 6))
plt.plot(X, Y, marker='o', linestyle='-', color='b')
plt.title('График зависимости Y от X')
plt.xlabel('X')
plt.ylabel('Y')
plt.xscale('log')
plt.grid(True)
plt.show()