"""
Визуализировать результаты работы методов в трёхмерном пространстве.
Построить разделяющие гиперплоскости между классами
"""



import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.svm import SVC  # <-- Добавляем импорт
from sklearn.inspection import DecisionBoundaryDisplay
import joblib
import pandas as pd


def plot_3d_decision_boundaries(model, X, y, title):
    fig = plt.figure(figsize=(14, 12))
    ax = fig.add_subplot(111, projection='3d')

    # Настройка внешнего вида
    ax.grid(False)
    for axis in [ax.xaxis, ax.yaxis, ax.zaxis]:
        axis.pane.fill = False
        axis.pane.set_edgecolor('w')

    # Цвета и маркеры
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1']
    markers = ['o', '^', 's']

    # Отображение исходных точек
    for i in range(3):
        ax.scatter(X[y == i, 0], X[y == i, 1], X[y == i, 2],
                   c=colors[i],
                   marker=markers[i],
                   label=f'Class {i}',
                   s=60,
                   edgecolor='w',
                   alpha=0.9)

    # Создание 3D сетки
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    z_min, z_max = X[:, 2].min() - 1, X[:, 2].max() + 1

    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 30),
                         np.linspace(y_min, y_max, 30))

    # Для SVM: Построение разделяющих гиперплоскостей
    if isinstance(model.named_steps['model'], SVC):  # Теперь SVC распознается
        # Вычисляем z-значения для гиперплоскостей
        for z_val in np.linspace(z_min, z_max, 5):
            zz = np.full_like(xx, z_val)
            grid = np.c_[xx.ravel(), yy.ravel(), zz.ravel()]
            preds = model.predict(grid).reshape(xx.shape)

            # Отображаем только границы классов
            ax.contourf(xx, yy, preds, zdir='z', offset=z_val,
                        alpha=0.15, colors=colors, levels=2)

    # Для KNN: Области классификации
    else:
        zz = np.linspace(z_min, z_max, 30)
        for z_val in zz[::5]:
            grid = np.c_[xx.ravel(), yy.ravel(), np.full_like(xx.ravel(), z_val)]
            preds = model.predict(grid).reshape(xx.shape)
            ax.contourf(xx, yy, preds, zdir='z', offset=z_val,
                        alpha=0.1, colors=colors, levels=2)

    # Настройки отображения
    ax.set_xlabel('X', fontsize=12, labelpad=15)
    ax.set_ylabel('Y', fontsize=12, labelpad=15)
    ax.set_zlabel('Z', fontsize=12, labelpad=15)
    ax.legend(loc='upper left', fontsize=12)
    ax.set_title(title, fontsize=16, pad=25)
    ax.view_init(elev=25, azim=-45)

    plt.tight_layout()
    plt.show()


# Загрузка данных и моделей
data = pd.read_csv('3d_classes.csv')
X = data[['x', 'y', 'z']].values
y = data['label'].values

knn_model = joblib.load('best_knn_model.pkl')
svm_model = joblib.load('best_svm_model.pkl')

# Визуализация
print("Визуализация для KNN:")
plot_3d_decision_boundaries(knn_model, X, y, 'KNN Decision Boundaries')

print("Визуализация для SVM:")
plot_3d_decision_boundaries(svm_model, X, y, 'SVM Decision Boundaries')