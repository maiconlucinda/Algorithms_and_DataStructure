
# 1 - Lista: Crie uma estrutura de repetição para fazer a leitura de 5 números inteiros e
# os armazene dentro de uma lista. Após a leitura, crie outra estrutura de repetição para
# somar todos os valores digitados

lista = []
for valor in range(0, 5):
    numero = int(input('Insira o número '))
    lista.append(numero)

result = 0
for valorIn in lista[0:5]:
    result += valorIn
print(result)






# 2 - Dicionário: Crie um dicionário para armazenar o nome e a nota de 3 alunos, fazendo a
# leitura dos valores por meio de uma estrutura de repetição. Depois, crie uma nova estrutura
# de repetição para somar todas as notas e retornar a média


dicio = {}
listaSequencia = ['primeiro/a', 'segundo/a', 'terceiro/a']
for indexValue in listaSequencia:
    nomeAluno = input(f'Insira o nome do {indexValue} Aluno ')
    notaAluno = input(f'Insira a nota do {indexValue} Aluno ')
    dicio[nomeAluno] = notaAluno
print(dicio.items())


value = 0
for _, grade in dicio.items():
    value += int(grade)

print(value)
print('\n')





# 3 - Matriz: Dada a matriz abaixo, construa uma estrutura de repetição para percorrer e somar todos os elementos da matriz

import numpy as np

matriz = np.array([[3, 4, 1],
                   [3, 1, 5]])

#resultante = 0
#for i in range(matriz.shape[0]):
#    for j in range(matriz.shape[1]):
#        resultante += int(matriz[i][j])

#print(resultante)

matriz = np.array([[3, 4, 1],
                   [3, 1, 5]])

for option in range(matriz.shape[0]):
    for opElement in range(matriz.shape[1]):
        result += int(matriz[option][opElement])





























