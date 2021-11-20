#Print normal
a = 'casaco'
print(a)


# Letras maiúsculas
maiuscula = a.upper()
print(maiuscula)


# Letras minúsculas
minuscula = maiuscula.lower()
print(minuscula)


# Capital (primeira letra maiúscula)
capital = a.capitalize()
print(capital)


# Pegar parte da palavra conforme o índice passado
metade_palavra = a[0:3]
print(metade_palavra)


# Pegar a partir de um determinado ponto até o final
ultimas_letras = a[3:]
print(ultimas_letras)


# Trocar parte da palavra
b = a.replace('aco', 'inha')
print(b)


# Trocando uma letra por outra
c = a.replace('o', 'a')
print(c)


# Encontrar determinado letra dentro de uma String
d = c.find('s')
print(d)


# Ver tamanho de uma String
e = ' casado '
print(len(e))



# Trabalhando com variáveis dentro uma string
n1 = 14
n2 = 16
print(f'Dividindo {n1} por {n2} o resultado é {n1/n2}')

