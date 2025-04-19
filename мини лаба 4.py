import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

housing_data = pd.read_csv('C:/Users/USER/PycharmProjects/pythonProject5/датасет-1.csv', sep=';')  # Путь к файлу
housing_data['price'] = housing_data['price'].str.replace(',', '.').astype(float)
housing_data['area'] = housing_data['area'].astype(float)

plt.figure(figsize=(10, 6))
plt.scatter(housing_data['area'], housing_data['price'], color='crimson', label='Исходные данные')
plt.xlabel('Площадь (кв.м.)', fontsize=12)
plt.ylabel('Стоимость (млн.руб)', fontsize=12)
plt.title('Зависимость стоимости от площади', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.show()

regression_model = LinearRegression()
regression_model.fit(housing_data[['area']], housing_data['price'])

small_apartment_size = 38
large_apartment_size = 200
predicted_price_small = regression_model.predict([[small_apartment_size]])[0]
predicted_price_large = regression_model.predict([[large_apartment_size]])[0]

print(f"Предсказанная цена квартиры {small_apartment_size} м²: {predicted_price_small:.2f} млн руб")
print(f"Предсказанная цена квартиры {large_apartment_size} м²: {predicted_price_large:.2f} млн руб")

# Параметры модели
print(f"Коэффициент наклона (a): {regression_model.coef_[0]:.4f}")
print(f"Коэффициент сдвига (b): {regression_model.intercept_:.4f}")


plt.figure(figsize=(10, 6))
plt.scatter(housing_data['area'], housing_data['price'], color='crimson', label='Исходные данные')
plt.plot(housing_data['area'], regression_model.predict(housing_data[['area']]),
         color='navy', linewidth=2, label='Линия регрессии')
plt.xlabel('Площадь (кв.м.)', fontsize=12)
plt.ylabel('Стоимость (млн.руб)', fontsize=12)
plt.title('Линейная регрессия: стоимость vs площадь', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.show()


new_apartments = pd.read_csv('C:/Users/USER/PycharmProjects/pythonProject5/prediction_price.csv')
price_predictions = regression_model.predict(new_apartments)
new_apartments['predicted_price'] = price_predictions


print("\nПрогнозируемые цены:")
print(new_apartments)

result_file = 'predicted_prices.xlsx'
new_apartments.to_excel(result_file, index=False)
print(f"\nРезультаты сохранены в файл: {result_file}")