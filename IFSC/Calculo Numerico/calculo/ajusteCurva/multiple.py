from pandas import DataFrame
from sklearn import linear_model
import statsmodels.api as sm
import numpy as np

data = {
    'Ano': [9, 14, 6, 11, 10, 8, 4],
    'Tamanho': [87, 86, 78, 94, 77, 104, 80],
    'Valor': [642, 464, 579, 550, 490, 710, 600]
}

df = DataFrame(data, columns=['Ano', 'Tamanho', 'Valor'])

X = df[['Ano', 'Tamanho']]
Y = df['Valor']

regr = linear_model.LinearRegression()
regr.fit(X, Y)

print(f'\nInterceptador: {regr.intercept_}')
print(f'\nCoeficientes (ŷ): {regr.coef_} \n')

# Previsão com sklearn
age = 12
size = 80
print(f'Indice de acao a ser previsto: {regr.predict([[age, size]])} \n')
print(f'R²: {regr.score(X, Y)} \n')
