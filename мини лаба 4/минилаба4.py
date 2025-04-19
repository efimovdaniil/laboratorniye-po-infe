import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model



df=pd.read_csv(r'датасет-1.csv',sep=';')



df['price']=df['price'].str.replace(',','.')
df['price']=df['price'].astype(float)


reg = linear_model.LinearRegression()
reg.fit(df[['area']],df.price)



pred = pd.read_csv(r'prediction_price.csv')


pred['area']=pred['area'].astype(float)


p = reg.predict(pred)
pred.to_excel('new.xlsx')
pred['predicted_prices'] = p
pred.to_excel('new.xlsx')




plt.scatter(df.area,df.price,color='red')
plt.scatter(pred.area,pred.predicted_prices,color = 'blue')
plt.xlabel('площадь(кв.м.)')
plt.ylabel('стоимость(млн.руб)')
plt.plot(pred.area, p)
plt.show()