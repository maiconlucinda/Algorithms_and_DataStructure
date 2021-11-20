

# Lógica é lógica - While quer dizer Enquanto, ou seja, enquanto algo estiver dentro das condições, teremos um ação.
# A estrutua for automaticamente incrementa o número, o While não, então cuidado com loops

# Do menor para o maior
numero = 1
while numero < 6:
    print(numero)
    numero += 1
print('----', '\n')


# Do maior para o menor
numero = 5
while numero > 0:
    print(numero)
    numero -= 1


# Exemplo para somar os valores
soma = 0
numero = 1
while numero < 6:
    soma += numero
    numero += 1
print(soma, '\n')



# Exemplo de validar até o que é esperado seja enviado.
numero = -1
while numero < 1 or numero > 10:
    numero = int(input('Digite um número de 1 a 10 '))