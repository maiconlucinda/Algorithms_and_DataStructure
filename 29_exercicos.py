
# 1 - Crie uma classe chamada aluno com os seguintes atributos:
# - Nome
# - Nota 1
# - Nota 2
# - Crie um construtor para a classe (__init__)


# 2 - Crie as seguintes funções (métodos):
# - Calcula média, retornando a média aritmética entre as notas
# - Mostra dados, que somente imprime o valor de todos os atributos
# - Resultado, que verifica se o aluno está aprovado ou reprovado
# (se a média for maior ou igual a 6.0, o aluno está aprovado)


# 3 - Crie dois objetos (aluno1 e aluno2) e teste as funções




class Aluno:

    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.medianota = 0.0


    def media(self):
        self.medianota = self.nota1 + self.nota2 / 2
        return self.medianota


    def dados(self):
        print(self.medianota)
        print('Nome:', self.nome)
        print('Nota 1:', self.nota1)
        print('Nota 2:', self.nota2)



    def aprovedornot(self):
        if self.medianota >= 6:
            print('Aluno Aprovado')
        else:
            print('Aluno Reprovado')


aluno1 = Aluno('Maicon', 8.9, 7)
print(aluno1.media())
aluno1.dados()
aluno1.aprovedornot()

print('\n')


aluno2 = Aluno('Julia', 2.2, 6.1)
print(aluno2.media())
aluno2.dados()
aluno2.aprovedornot()













