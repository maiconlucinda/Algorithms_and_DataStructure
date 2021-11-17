
# Implementação do vetor não odernado

import numpy as np

# O primeiro passo é criar a classe, pois assim será possível trabalhar com uma implementação única, sem repetição
# de código, abstraindo toda a ideia do mundo real, no mundo isso seria a ideia de criarmos uma espécie de armario para
# guardar informações, as funções que esse armario terá, serão baseadas nos métodos que criaremos, mesma coisa se trata
# das propriedades desse armario, também teremos as informações para isso.

class VetorNaoOrdenado:

    # A primeira função que precisa existir é a função de construção desse armario (chamado de método construtor),
    # sem essa função que tem a capacidade de ser chamada automaticamente, não é possível criar o armario que precisamos,
    # para esse primeiro método precisamos enviar a capacidade desse nosso armario, e também dizer o tipo de dados que
    # será permitido colocar nele.

    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade, dtype=int)



    # Criamos também um método (função) para que o próprio armario tenha a capacidade de nos dizer quais posições estão
    # ocupadas.
    # Big-O igual o(n)
    def imprimir(self):
        if self.ultima_posicao == -1:
            print('O vetor está vazio')
        else:
            for i in range(self.ultima_posicao + 1):
                print(i, '-', self.valores[i])


    # O que preciso fazer?
    # 1 - Preciso receber os valores enviado pelo usuário
    # 2 - Preciso analisar qual está sendo a última posição ocupada da estrutura
    # 3 - Preciso inserir o valor recebido nesta estrutura
    # Big-O O(1)
    def insercao(self, valoraseradicionado):
        if self.ultima_posicao == self.capacidade - 1:
            print('Capacidade máxima atingida')
        else:
            self.ultima_posicao += 1
            self.valores[self.ultima_posicao] = valoraseradicionado



    # O que preciso fazer?
    # 1 - Preciso validar se a estrutura está com a última posição = -1, pois se tiver significa que está vazia
    # 2 - Preciso primeiramente validar qual a última posição alocada na estrutura
    # 3 - Preciso percorrer até a última posição + 1 validando se procurado o elemento está inserido
    # Big-O = O(n)
    def pesquisa(self, valorprocurado):
        for i in range(self.ultima_posicao + 1):
            if valorprocurado == self.valores[i]:
                return i
        # Caso o if em nehum momento seja true, no final será retornado -1
        return -1



    # O que preciso fazer?
    # 1 - Preciso validar se a estrutura está com a última posição = -1, pois se tiver significa que está vazia
    # 2 - Preciso criar um loop para enquanto posição for menor que ultima posição, reallizar ação de trazer os valores para uma posição anterior
    def exclusao(self, valor):
        posicao = self.pesquisa(valor)
        if posicao == -1:
            return -1
        else:
            while posicao < self.ultima_posicao:
                self.valores[posicao] = self.valores[posicao + 1]
                posicao += 1
            self.ultima_posicao -= 1


vetor = VetorNaoOrdenado(5)
vetor.insercao(8)
vetor.insercao(7)
vetor.insercao(9)
vetor.insercao(1)
vetor.insercao(2)
#print(vetor.pesquisa(7))
vetor.exclusao(8)

vetor.imprimir()



# Anotações
# A inserção