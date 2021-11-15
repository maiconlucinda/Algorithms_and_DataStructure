
# Por que usar estrutura de repetição?
# Não precisar digitar um mesmo código várias vezes
print(1)
print(2)
print(3)
print(4)
print(5)
print('\n')


# FOR
# Tradução: PARA UM numero que está na FAIXA(1, 5)
for number in range(1, 5):
    print(number)
print('\n')



# FOR AO CONTRÁRIO
# Para fazer ao contrário, é necessário passar um terceiro parametro que é o Step, ou seja, -1
for number in range(5, 0, -1):
    print(number)
print('\n')




# Executando um código para somar 1 + 2 +3 + 4 + 5
soma = 0
for number in range(1, 6):
    soma = soma + number
print(soma, '\n')



# Exemplo de for em uma palavra ou texto para validar se há um determinada letra dentro
palavra = 'sorvete'
for letra in palavra:
    if letra == "v":
        print('Acho a letra V', '\n')



# Exemplo de for aninhado para percorrer matrizes
for i in range(0, 5):
    print(i)
    print('----')
    for j in range(0, 3):
        print(j)
    print()
