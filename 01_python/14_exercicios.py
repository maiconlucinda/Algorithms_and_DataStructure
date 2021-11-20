
# 1 - Lista: Crie uma estrutura de repetição para fazer a leitura de 5 números inteiros e
# os armazene dentro de uma lista. Após a leitura, crie outra estrutura de repetição para
# somar todos os valores digitados

lista = []
for valor in range(0, 5):
    numero = int(input('Insira o número '))
    lista.append(numero)

result = 0
for valorIn in range(len(lista)):
    result += lista[valorIn]
print(result)
# Fazendo a soma de uma maneira um pouco diferente
import numpy as np
print(np.array(lista).sum()) # Ao converter para array usando o numpy, terei mais métodos para chamar.




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

print(value / 3)
print('\n')





# 3 - Matriz: Dada a matriz abaixo, construa uma estrutura de repetição para percorrer e somar todos os elementos da matriz

matriz = np.array([[3, 4, 1],
                   [3, 1, 5]])

totalValue = 0
for valueLine in range(matriz.shape[0]):
    for valueColumn in range(matriz.shape[1]):
        totalValue += int(matriz[valueLine][valueColumn])

print(totalValue)





















