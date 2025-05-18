import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
import random


def original_function(x):
    return np.sin(x / 2) + 0.5 * np.sqrt(np.abs(x)) + 0.1 * x ** 2

np.random.seed(42)
x_min, x_max = -10, 10
x = np.linspace(x_min, x_max, 100).reshape(-1, 1)
y_true = original_function(x)
noise = np.random.uniform(-1, 1, size=x.shape)
y = y_true + noise

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

models = [
    ("Линейная регрессия", LinearRegression()),
    ("Поддержка векторов (SVR)", SVR(kernel='rbf', C=100, gamma=0.1, epsilon=0.1)),
    (
    "Градиентный бустинг", GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42))
]

plt.figure(figsize=(18, 6))
for i, (name, model) in enumerate(models):
    # Обучение модели
    model.fit(x_train, y_train.ravel())
    y_pred = model.predict(x)

    mse = mean_squared_error(y_true, y_pred)

    plt.subplot(1, 3, i + 1)
    plt.scatter(x, y, color='blue', alpha=0.5, label='Исходные точки с шумом')
    plt.plot(x, y_true, color='green', linewidth=2, label='Исходная функция')
    plt.plot(x, y_pred, color='red', linewidth=2, label='Предсказание модели')
    plt.title(f'{name}\nMSE: {mse:.4f}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)

plt.tight_layout()
plt.show()

print("\nРезультаты на тестовой выборке:")
for name, model in models:
    y_test_pred = model.predict(x_test)
    mse_test = mean_squared_error(y_test, y_test_pred)
    print(f"{name}: MSE = {mse_test:.4f}")