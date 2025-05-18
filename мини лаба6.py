import numpy as np
import matplotlib.pyplot as plt


def gradientDescend(func=lambda x: x ** 2, diffFunc=lambda x: 2 * x, x0=3, speed=0.01, epochs=100):
    x_list = []
    y_list = []
    x = x0

    for _ in range(epochs):
        x_list.append(x)
        y_list.append(func(x))
        x = x - speed * diffFunc(x)

    return x_list, y_list


def my_func(x):
    return np.exp(-x / 5) * np.sin(x) + x ** 2 / 20


def my_func_derivative(x):
    return -1 / 5 * np.exp(-x / 5) * np.sin(x) + np.exp(-x / 5) * np.cos(x) + x / 10

x_vals, y_vals = gradientDescend(my_func, my_func_derivative, x0=1, speed=0.1, epochs=50)

x = np.linspace(-3, 3, 400)
y = my_func(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y, label='f(x) = e^(-x/5)*sin(x) + x²/20')
plt.scatter(x_vals, y_vals, color='red', label='Точки градиентного спуска')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Градиентный спуск')
plt.legend()
plt.grid(True)
plt.show()

final_x = x_vals[-1]
print(f"Финальная точка: x = {final_x:.4f}, f(x) = {my_func(final_x):.4f}")
print(f"Минимум функции находится примерно в x ≈ -1.3")
print("Результат работы сходится к искомому минимуму? ", "Да" if abs(final_x - (-1.3)) < 0.5 else "Нет")


def find_critical_speed(func, diffFunc, x0=1, target=-1.3, tol=0.1):
    low = 0.01
    high = 1.0
    best_speed = low

    for _ in range(20):
        mid = (low + high) / 2
        x_vals, _ = gradientDescend(func, diffFunc, x0, mid, 50)
        final_x = x_vals[-1]

        if abs(final_x - target) < tol:
            best_speed = mid
            low = mid
        else:
            high = mid

    return best_speed


critical_speed = find_critical_speed(my_func, my_func_derivative)
print(f"\nГраничное значение speed: ≈{critical_speed:.4f}")
print(f"При speed < {critical_speed:.4f} метод сходится, при speed > {critical_speed:.4f} - расходится")