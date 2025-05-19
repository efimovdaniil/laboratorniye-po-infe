"""
Разделить исходные данные на обучающую и тестовую выборки. Создать модели k ближайших соседей (KNN) и метода опорных векторов (SVM).
Подобрать эффективные параметры для этих методов с применением поиска по сетке (Grid Search)
"""


import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

# 1. Загрузка данных
data = pd.read_csv('3d_classes.csv')
X = data[['x', 'y', 'z']].values
y = data['label'].values

# 2. Разделение данных
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.3,
    stratify=y,
    random_state=42
)

# 3. Создание пайплайнов с масштабированием данных
knn_pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('model', KNeighborsClassifier())
])

svm_pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('model', SVC())
])

# 4. Параметры для Grid Search
knn_params = {
    'model__n_neighbors': [3, 5, 7, 9, 11],
    'model__weights': ['uniform', 'distance'],
    'model__algorithm': ['auto', 'ball_tree', 'kd_tree']
}

svm_params = {
    'model__C': [0.1, 1, 10, 100],
    'model__kernel': ['linear', 'rbf', 'poly'],
    'model__gamma': ['scale', 'auto']
}

# 5. Поиск лучших параметров для KNN
knn_gs = GridSearchCV(
    estimator=knn_pipeline,
    param_grid=knn_params,
    cv=5,
    n_jobs=-1,
    verbose=1
)
knn_gs.fit(X_train, y_train)

# 6. Поиск лучших параметров для SVM
svm_gs = GridSearchCV(
    estimator=svm_pipeline,
    param_grid=svm_params,
    cv=5,
    n_jobs=-1,
    verbose=1
)
svm_gs.fit(X_train, y_train)

# 7. Оценка моделей
def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Лучшие параметры: {model.best_params_}")
    print(f"Точность на тестовых данных: {accuracy:.4f}\n")

print("Результаты для KNN:")
evaluate_model(knn_gs, X_test, y_test)

print("Результаты для SVM:")
evaluate_model(svm_gs, X_test, y_test)
# 8. Сохранение лучших моделей
import joblib
joblib.dump(knn_gs.best_estimator_, 'best_knn_model.pkl')
joblib.dump(svm_gs.best_estimator_, 'best_svm_model.pkl')
