
# Abrindo um arquivo de texto e realizando um for em cada linha to arquivo
with open('frase1.txt') as tex:
    for linha in tex:
        print(linha)


# Abrindo um arquivo de texto e adicionando cada linha do arquivo dentro de uma lista.
with open('frase1.txt') as tex2:
    for cadalinha in tex2:
        r = tex2.readlines()
print(r)


# Criando um arquivo txt com a linguagem Python (necessário colocar o mode w, quer dizer write)
with open('frase2.txt', 'w') as texto:
    texto.write('Olá a todos')


