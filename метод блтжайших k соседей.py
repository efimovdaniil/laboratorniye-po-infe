import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

def generate_data(pointsCount1, pointsCount2, xMin1, xMax1, yMin1, yMax1, xMin2, xMax2, yMin2, yMax2):
    x1 = np.random.uniform(xMin1, xMax1, (pointsCount1, 2))
    x2 = np.random.uniform(xMin2, xMax2, (pointsCount2, 2))
    x = np.concatenate((x1, x2), axis=0)
    y = np.concatenate((np.zeros(pointsCount1), np.ones(pointsCount2)))
    return x, y

def train_test_split(x, y, p=0.8):
    indices = np.random.permutation(len(x))
    train_size = int(len(x) * p)
    train_indices = indices[:train_size]
    test_indices = indices[train_size:]
    x_train, x_test = x[train_indices], x[test_indices]
    y_train, y_test = y[train_indices], y[test_indices]
    return x_train, x_test, y_train, y_test

def euclidean_distance(x1, x2):
    return np.sqrt(np.sum((x1 - x2)**2))

def fit(x_train, y_train, x_test, k=3):
    y_predict = []
    for test_point in x_test:
        distances = [euclidean_distance(test_point, train_point) for train_point in x_train]
        k_nearest_indices = np.argsort(distances)[:k]
        k_nearest_labels = [y_train[i] for i in k_nearest_indices]
        most_common = Counter(k_nearest_labels).most_common(1)[0][0]
        y_predict.append(most_common)
    return np.array(y_predict)

def computeAccuracy(y_test, y_predict):
    correct_predictions = np.sum(y_test == y_predict)
    accuracy = correct_predictions / len(y_test)
    return accuracy


pointsCount1, pointsCount2 = 50, 50
xMin1, xMax1, yMin1, yMax1 = 1, 6, 1, 6
xMin2, xMax2, yMin2, yMax2 = 2, 8, 2, 8

x, y = generate_data(pointsCount1, pointsCount2, xMin1, xMax1, yMin1, yMax1, xMin2, xMax2, yMin2, yMax2)
x_train, x_test, y_train, y_test = train_test_split(x, y)
y_predict = fit(x_train, y_train, x_test)
accuracy = computeAccuracy(y_test, y_predict)

print(f"Accuracy: {accuracy}")


plt.figure(figsize=(8, 6))
plt.scatter(x_train[y_train == 0][:, 0], x_train[y_train == 0][:, 1], marker='o', c='blue', label='Train Class 0')
plt.scatter(x_train[y_train == 1][:, 0], x_train[y_train == 1][:, 1], marker='x', c='blue', label='Train Class 1')

correct_0 = (y_test == 0) & (y_predict == y_test)
incorrect_0 = (y_test == 0) & (y_predict != y_test)
correct_1 = (y_test == 1) & (y_predict == y_test)
incorrect_1 = (y_test == 1) & (y_predict != y_test)

plt.scatter(x_test[correct_0][:, 0], x_test[correct_0][:, 1], marker='o', c='green', label='Correct Test Class 0')
plt.scatter(x_test[correct_1][:, 0], x_test[correct_1][:, 1], marker='x', c='green', label='Correct Test Class 1')
plt.scatter(x_test[incorrect_0][:, 0], x_test[incorrect_0][:, 1], marker='o', c='red', label='Incorrect Test Class 0')
plt.scatter(x_test[incorrect_1][:, 0], x_test[incorrect_1][:, 1], marker='x', c='red', label='Incorrect Test Class 1')

plt.legend()
plt.title('KNN Classification Results')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()