
alunos = {'Pedro': 8.0, 'Maria': 10.0, 'Amilton': 7.5}

with open('alunos_notas.txt', 'w') as informacoes:
    for nome, nota in alunos.items():
        informacoes.write(f"{nome},{nota}\n")

with open('alunos_notas.txt') as leitura:
    for linha in leitura:
        print(linha)


