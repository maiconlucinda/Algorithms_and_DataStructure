
# Biblioteca muito utilizada para processamento cientifico
import numpy as np

# Criando um matriz para receber a função array da Biblioteca Numpy, ao mesmo tempo passando alguns valores como parametros.
# A velocidade do processamento é maior com essa estrutura de dados.
matriz = np.array([[2, 3, 1],
                   [4, 5, 7]])
# Foi criado uma matriz que tem duas linha e tres colunas.
print(matriz)
print('\n')

# Comando para retornar sobre a composição da matriz
print(matriz.shape)
print('\n')

# Posso acessar posições específicas de dentro da Matriz
print(matriz[0])
print(matriz[1])

# Posso acessar valores de dentro dos arrays das matrizes
print(matriz[0][1])
print('\n')

# Digamos que seja necessário executar algum tipo de calculo sobre cada valor inseridos dentro dos elementos de uma matriz, como pode ser feito?
#for i in range(matriz.shape[0]): # utilizando o shape, consigo pegar a quantidade de linhas e também de colunas, peguei o número de linhas.
#    print(matriz[i])
#    for j in range(matriz.shape[1]):
#        print(matriz[i][j])









