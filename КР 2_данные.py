"""
Контрольная работа 2. Классификация
Сгенерировать 3 класса точек в трёхмерном пространстве без пересечений.
Сохранить полученные данные в файл
"""


import numpy as np
import csv
from sklearn.utils import shuffle

# Параметры генерации
num_points = 100  # Количество точек в каждом классе
std_dev = 1.5     # Стандартное отклонение для разброса точек
centers = [       # Центры кластеров
    [0, 0, 0],
    [10, 10, 10],
    [-10, 0, 10]
]

# Генерация данных
data = []
labels = []

for class_label, center in enumerate(centers):
    # Генерируем точки с нормальным распределением вокруг центра
    points = np.random.normal(loc=center, scale=std_dev, size=(num_points, 3))
    data.extend(points)
    labels.extend([class_label] * num_points)

# Преобразуем в numpy array и перемешиваем
data = np.array(data)
labels = np.array(labels)
data, labels = shuffle(data, labels, random_state=42)

# Объединяем данные и метки
full_data = np.hstack((data, labels.reshape(-1, 1)))

# Сохраняем в CSV файл
header = ['x', 'y', 'z', 'label']

with open('3d_classes.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(full_data)

print("Данные сохранены в файл '3d_classes.csv'")