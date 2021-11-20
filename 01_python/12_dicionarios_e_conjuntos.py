
# TUPLAS UTILIZAMOS ()
# LISTAS UTILIZAMOS []
# DICIONÁRIOS UTILIZAMOS {}


# DICIONÁRIO
# Dicionário tem um nome e tem um valor na frente (ideia de chave valor)
quantidadeDeAmostraColetada = {'Aedes aegypt': 32, 'Aedes albopictus': 22, 'Anopeles darlingi': 14}
print(quantidadeDeAmostraColetada['Aedes aegypt'])

# Adicionando novos elementos
quantidadeDeAmostraColetada['Rhodnuis montenegrensis'] = 11
print(quantidadeDeAmostraColetada)
print('\n')

# Apagando um elemento
del(quantidadeDeAmostraColetada)['Aedes aegypt']
print(quantidadeDeAmostraColetada)
print('\n')

# Output em um formato diferente
print(quantidadeDeAmostraColetada.items())
print('\n')

# Posso ver que é de fato um dicionário, pois tem chave e valor
print(quantidadeDeAmostraColetada.keys())
print(quantidadeDeAmostraColetada.values())
print('\n')

quantidadeDeAmostraColetada2 = {'Jonatas Machado': 31, 'Rosangela Machado': 26}
# Concatenando dicionários
quantidadeDeAmostraColetada.update(quantidadeDeAmostraColetada2)
print(quantidadeDeAmostraColetada)

#Percorrendo um dicionário - Acessando
print(quantidadeDeAmostraColetada.items())

for nome, quantidade in quantidadeDeAmostraColetada.items():
    print(f"Nome: {nome}, Quantidade: {quantidade}")
print('\n')







# CONJUNTOS
# De inicio, tudo se parece uma tupla normal
componentes = ('teclado', 'mouse', 'nonitor', 'fonte de energia',
               'teclado', 'mouse', 'monitor', 'fonte de energia')

# Ao utilizar o Set, estamos trabalhando com conjuntos, teremos somente os valores que não se repetem.
print(set(componentes))
print('\n')

conjunto1 = {1,2,3,4,5}
conjunto2 = {3,4,5,6,7}
conjunto3 = conjunto1.intersection(conjunto2) # Comando para fazer uma intersecção entre os conjuntos
print(conjunto3)
print('\n')

print(conjunto1.difference(conjunto2)) # Comando para ver a diferença entre os conjuntos





