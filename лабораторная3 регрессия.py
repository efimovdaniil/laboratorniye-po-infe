import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Параметры задачи
a_true = 2.0  # Истинное значение амплитуды
b_true = 1.5  # Истинное значение частоты
c_true = 3.0  # Истинное значение смещения

# Генерация данных с шумом
np.random.seed(42)
x_min, x_max, points = 0, 10, 50
x = np.linspace(x_min, x_max, points)
e = np.random.uniform(-3, 3, points)
y = a_true * np.sin(b_true * x) + c_true + e


# Функция для расчета MSE
def calculate_mse(a, b, c, x, y):
    y_pred = a * np.sin(b * x) + c
    return np.mean((y_pred - y) ** 2)


# Функции для частных производных
def dJ_da(a, b, c, x, y):
    return 2 * np.mean((a * np.sin(b * x) + c - y) * np.sin(b * x))


def dJ_db(a, b, c, x, y):
    return 2 * np.mean((a * np.sin(b * x) + c - y) * a * x * np.cos(b * x))


def dJ_dc(a, b, c, x, y):
    return 2 * np.mean(a * np.sin(b * x) + c - y)


# Градиентный спуск
def gradient_descent(x, y, learning_rate=0.01, epochs=1000):
    # Инициализация параметров
    a = 1.0
    b = 1.0
    c = 1.0

    # Для хранения истории параметров и MSE
    history = []

    for epoch in range(epochs):
        # Вычисление градиентов
        grad_a = dJ_da(a, b, c, x, y)
        grad_b = dJ_db(a, b, c, x, y)
        grad_c = dJ_dc(a, b, c, x, y)

        # Обновление параметров
        a -= learning_rate * grad_a
        b -= learning_rate * grad_b
        c -= learning_rate * grad_c

        # Сохранение истории
        mse = calculate_mse(a, b, c, x, y)
        history.append({'epoch': epoch, 'a': a, 'b': b, 'c': c, 'mse': mse})

    return a, b, c, history


# Запуск градиентного спуска
learning_rate = 0.01
epochs = 1000
a_opt, b_opt, c_opt, history = gradient_descent(x, y, learning_rate, epochs)

# Визуализация
fig, ax = plt.subplots(figsize=(10, 6))
plt.subplots_adjust(bottom=0.25)

# Исходные данные
scatter = ax.scatter(x, y, color='red', label='Исходные данные')

# Кривая регрессии
x_fit = np.linspace(x_min, x_max, 100)
y_fit = a_opt * np.sin(b_opt * x_fit) + c_opt
line, = ax.plot(x_fit, y_fit, 'b-', label=f'Оптимальная модель: {a_opt:.2f}*sin({b_opt:.2f}x) + {c_opt:.2f}')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Гармоническая регрессия: y = a*sin(bx) + c')
ax.legend()
ax.grid(True)

# Создание слайдера
ax_slider = plt.axes([0.2, 0.1, 0.6, 0.03])
slider = Slider(ax_slider, 'Итерация', 0, epochs - 1, valinit=epochs - 1, valstep=1)


def update(val):
    iteration = int(slider.val)
    params = history[iteration]
    y_fit = params['a'] * np.sin(params['b'] * x_fit) + params['c']
    line.set_ydata(y_fit)
    line.set_label(f'Итерация {iteration}: a={params["a"]:.2f}, b={params["b"]:.2f}, c={params["c"]:.2f}')
    ax.legend()
    fig.canvas.draw_idle()


slider.on_changed(update)
plt.show()

# Вывод оптимальных параметров
print(f"Оптимальные параметры:")
print(f"a = {a_opt:.4f}")
print(f"b = {b_opt:.4f}")
print(f"c = {c_opt:.4f}")
print(f"Минимальная MSE = {calculate_mse(a_opt, b_opt, c_opt, x, y):.4f}")