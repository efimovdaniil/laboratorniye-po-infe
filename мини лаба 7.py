import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam

plt.figure(figsize=(18, 25))
plt.suptitle("Сравнение методов классификации на различных наборах данных", y=1.02, fontsize=16)

methods = [
    ("K-ближайших соседей", KNeighborsClassifier(n_neighbors=3)),
    ("Метод опорных векторов", SVC(kernel='rbf', C=1.0)),
    ("Многослойный перцептрон (Keras)", None)
]

datasets_list = [
    ("Две окружности", datasets.make_circles(n_samples=500, factor=0.5, noise=0.05, random_state=30)),
    ("Две параболы", datasets.make_moons(n_samples=500, noise=0.05, random_state=30)),
    ("Немного хаотичное распределение",
     datasets.make_blobs(n_samples=500, cluster_std=[1.0, 0.5], random_state=30, centers=2)),
    ("Точки вокруг прямых", None),  # Создадим отдельно
    ("Слабо пересекающиеся области", datasets.make_blobs(n_samples=500, random_state=30, centers=2))
]

x, y = datasets.make_blobs(n_samples=500, random_state=170, centers=2)
transformation = [[0.6, -0.6], [-0.4, 0.8]]
x_aniso = np.dot(x, transformation)
datasets_list[3] = ("Точки вокруг прямых", (x_aniso, y))

for row, (dataset_name, (x, y)) in enumerate(datasets_list):
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)


    temp_x = np.linspace(x[:, 0].min() - 1, x[:, 0].max() + 1, 100)
    temp_y = np.linspace(x[:, 1].min() - 1, x[:, 1].max() + 1, 100)
    xx, yy = np.meshgrid(temp_x, temp_y)

    for col, (method_name, model) in enumerate(methods):
        plt.subplot(5, 3, row * 3 + col + 1)

        if method_name == "Многослойный перцептрон (Keras)":
            keras_model = Sequential([
                Dense(64, activation='relu', input_shape=(2,)),
                Dense(32, activation='relu'),
                Dense(1, activation='sigmoid')
            ])
            keras_model.compile(optimizer=Adam(0.001), loss='binary_crossentropy', metrics=['accuracy'])
            keras_model.fit(x_train, y_train, epochs=15, batch_size=32, verbose=0)

            Z = keras_model.predict(np.c_[xx.ravel(), yy.ravel()])
            Z = (Z > 0.5).astype(int).reshape(xx.shape)

            y_pred = (keras_model.predict(x_test) > 0.5).astype(int).flatten()
        else:
            model.fit(x_train, y_train)

            Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
            Z = Z.reshape(xx.shape)

            y_pred = model.predict(x_test)

        accuracy = accuracy_score(y_test, y_pred)

        plt.contourf(xx, yy, Z, alpha=0.3, cmap='bwr')

        for i in range(len(x_train)):
            plt.scatter(x_train[i, 0], x_train[i, 1],
                        marker='x' if y_train[i] == 0 else 'o',
                        c='blue', alpha=0.5)

        for i in range(len(x_test)):
            color = 'green' if y_test[i] == y_pred[i] else 'red'
            plt.scatter(x_test[i, 0], x_test[i, 1],
                        marker='x' if y_test[i] == 0 else 'o',
                        c=color, edgecolors='k')

        plt.title(f"{dataset_name}\n{method_name}\nТочность: {accuracy:.2f}")
        plt.xlabel("Признак 1")
        plt.ylabel("Признак 2")

plt.tight_layout()
plt.show()