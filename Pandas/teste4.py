"""
https://pandas.pydata.org/pandas-docs/stable/user_guide/basics.html#iteration
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.iterrows.html
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.items.html
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.itertuples.html
"""

import pandas as pd

dados = {
    'Motor': ['Motor 4.0 Turbo', 'Motor Diesel', 'Motor Diesel V8', 'Motor Diesel', 'Motor 1.6'],
    'Ano': [2019, 2003, 1991, 2019, 1990],
    'Quilometragem': [0.0, 5712.0, 37123.0, 0.0, 120000.0],
    'Zero_km': [True, False, False, True, False],
    'Valor': [88000.0, 106000.0, 72000.0, 89000.0, 32000.0]
}

dataset = pd.DataFrame(dados, index = ['Jetta', 'Passat', 'Crossfox', 'DS5', 'Fusca'])


# for a, b in dataset.iterrows():
#     print(a, b)

print(dataset.itertuples())