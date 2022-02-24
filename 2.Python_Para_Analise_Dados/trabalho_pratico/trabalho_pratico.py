'''
    Modulo 2: Python para a Análise de Dados 
              Trabalho Pratico

    Objetivos:
        Criação e manipulação de numpy arrays.
        Leitura de dados e manipulação de DataFrames e Series no pandas.
        Fundamentos de aprendizado de máquinas 
'''

#bibliotecas 
import numpy as np 
import pandas as pd 


# == CODIGO 01 == #
Z = np.zeros((4,))
print('codigo 01 - Z: ', Z)
print('\n')

# == CODIGO 02 == #
Z = np.zeros((4,))
Z[1] = 1.
print('codigo 02 - Z: ', Z)
print('\n')

# == CODIGO 03 == #
Z = np.zeros((4,))
Z[1:] = 1.
print('codigo 03 - Z: ', Z)
print('\n')

# == CODIGO 04 == #
Z = np.zeros((4,))
Z[:-1] = 1.
print(' codigo 04 - Z: ', Z)
print('\n')

# == CODIGO 05 == #
X = np.ones((2,2)) + 1
print('codigo 05 - X:  \n', X)
print('\n')

# == CODIGO 06 == #
X = np.array([[1,2], [3,4]])
Y = X[0,:]
Y[1] = 10
print('codigo 06 - X: \n', X)
print('\n')

# == CODIGO 07 == #
X = np.array([[1,3], [11,10]])
print("codigo 07 - ")
print(np.mean(X[X > np.pi]))
print('\n')

# == CODIGO 08 == #
data = {
    'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
    'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
    'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']
}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']


# == CODIGO 09 == #
df = pd.DataFrame(data = data, index = labels)
print("codigo 8 e 9 - ")
print(df)
print("\n")
print(df.shape)
print("\n")
print(df['animal'].value_counts())

# == CODIGO 10 == #
y_true = np.array([1., 2., 1.])
y_pred = np.array([1.1, 1.98, 1.05])

