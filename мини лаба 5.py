import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import Adam



def generate_datasets():
    dataset = []


    X, y = datasets.make_circles(n_samples=500, factor=0.5, noise=0.05, random_state=30)
    dataset.append(('Circles', X, y))


    X, y = datasets.make_moons(n_samples=500, noise=0.05, random_state=30)
    dataset.append(('Moons', X, y))


    X, y = datasets.make_blobs(n_samples=500, cluster_std=[1.0, 0.5], random_state=30, centers=2)
    dataset.append(('Varied Blobs', X, y))


    X, y = datasets.make_blobs(n_samples=500, random_state=170, centers=2)
    transformation = [[0.6, -0.6], [-0.4, 0.8]]
    dataset.append(('Anisotropic', np.dot(X, transformation), y))


    X, y = datasets.make_blobs(n_samples=500, random_state=30, centers=2)
    dataset.append(('Overlapping', X, y))

    return dataset



models = [
    ('SVM (RBF)', SVC(kernel='rbf', C=1.0)),
    ('Decision Tree', DecisionTreeClassifier(max_depth=5, criterion='entropy', random_state=42)),
    ('MLP Keras', None)  # Будет переопределена
]


fig, axes = plt.subplots(5, 3, figsize=(20, 25))
plt.subplots_adjust(wspace=0.3, hspace=0.4)


for row, (name, X, y) in enumerate(generate_datasets()):

    X = StandardScaler().fit_transform(X)


    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 100),
                         np.linspace(y_min, y_max, 100))

    for col, (model_name, model) in enumerate(models):
        ax = axes[row, col]


        if model_name == 'MLP Keras':
            model = Sequential([
                Dense(64, activation='relu', input_shape=(2,)),
                Dropout(0.3),
                Dense(32, activation='relu'),
                Dense(1, activation='sigmoid')
            ])
            model.compile(optimizer=Adam(0.001),
                          loss='binary_crossentropy',
                          metrics=['accuracy'])
            model.fit(X_train, y_train, epochs=20, batch_size=32, verbose=0)
            Z = model.predict(np.c_[xx.ravel(), yy.ravel()]) > 0.5
        else:
            model.fit(X_train, y_train)
            Z = model.predict(np.c_[xx.ravel(), yy.ravel()])


        Z = Z.reshape(xx.shape)
        ax.contourf(xx, yy, Z, alpha=0.3, cmap='coolwarm')


        ax.scatter(X_train[:, 0], X_train[:, 1], c=y_train, cmap='coolwarm', edgecolors='k', s=40)


        y_pred = model.predict(X_test)
        incorrect = (y_pred != y_test)
        ax.scatter(X_test[0], X_test[1],
                   color='red', marker='x', s=100, linewidth=2)


        ax.set_xlim(xx.min(), xx.max())
        ax.set_ylim(yy.min(), yy.max())
        ax.set_xticks([])
        ax.set_yticks([])

        if row == 0:
            ax.set_title(model_name, fontsize=14, pad=20)
        if col == 0:
            ax.set_ylabel(name, rotation=0, fontsize=12, labelpad=40)

plt.suptitle("Сравнение методов классификации на различных наборах данных", y=0.99, fontsize=16)
plt.show()