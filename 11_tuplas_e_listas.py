
# O QUE SÃO COLEÇÕES?
    # São diferentes tipos de variáveis das que utilizamos geralmente, pois quando criamos uma variável comum,
    # dizemos que A recebe 5 e pronto.


# TUPLA (a ideia é parecida com a ideia do Array)
tupla = ('Maicon Lucinda', 'Rosilene Santos da Cruz', 'Ademir Lucinda Augusto')
# Acessando a tupla utilizando a posição
print(tupla[1])
# Acessando a tupla pelo 'nome' para encontrar o valor do índice
print(tupla.index('Maicon Lucinda'))

# Percorrer elementos de uma Tupla
for element in tupla:
    print(element)





# Lista (a ideia também é parecida com a ideia do Array)
list1 = ['Maicon Lucinda', 'Rosilene Santos da Cruz', 'Ademir Lucinda Augusto']
list2 = ['ISH Tecnologia', 'Facebook']

# Concatenando as listas
list3 = list1 + list2
print(list3)
print('\n')

# Multiplicando as listas
list2_2 = list2 * 2
print(list2_2)
print('\n')

# Acessando elementos da lista
print(list2[1])
print('\n')

# Acessando somente alguns elementos
print(list1[0:2])

# Adicionando elementos dentro da lista
list1.append('Amanda Lucinda da Cruz')
print(list1)
print('\n')

# Removendo elemento dentro da lista
list1.remove('Maicon Lucinda')
print(list1)
print('\n')

del(list2)
#print(list1)

for item in list1:
    print(item)


# TUPLAS UTILIZAMOS ()
# LISTAS UTILIZAMOS []
# DICIONÁRIOS UTILIZAMOS {}





