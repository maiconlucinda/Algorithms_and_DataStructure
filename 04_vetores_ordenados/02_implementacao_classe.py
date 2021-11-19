
# importar tudos os módulos que serão necessário utilizar
import numpy as np

class VetorOrdenado:

    # O primeiro método precisa ser o construtor, esse irá definir as propriedades para o escopo.
    # Irá também criar a estrutura necessária
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        # Não posso criar a estrutura me baseando no valor capacidades, pois ele será alterado por outros métodos também
        self.valores = np.empty(self.capacidade, dtype=int)


    def imprimir(self):
        if self.ultima_posicao == -1:
            print('O vetor está vazio')
        else:
            for i in range(self.ultima_posicao + 1):
                print(i, '-', self.valores[i])


    # 1 - Caso o valor do última posição seja igual a -1, posso retornar -1, para dizer que não existe ese valor dentro.
    # 2 - Loop para buscar até a última posição, algum valore que corresponda ao valor procurado
    # 3 - Caso o valor seja encontrado, retorne a posição do mesmo.
    def pesquisa(self, valor):
        if self.ultima_posicao == -1:
            return self.ultima_posicao
        else:
            for i in range(self.ultima_posicao + 1):
                if valor == self.valores[i]:
                    return i
            return -1


    # Big-O = O(n)
    def insercao(self, valor):

        # Caso a estrutura estiver cheia
        if self.ultima_posicao == self.capacidade - 1:
            print('Vetor atingiu capacidade máxima')
            return

        # Maneira de encontrar a posição onde o valor deverá ficar
        posicao = 0
        for i in range(self.ultima_posicao + 1):
            posicao = i
            if self.valores[i] > valor:
                break
            if i == self.ultima_posicao:
                posicao = i + 1

        # Movendo os valores para um posicao a frente
        x = self.ultima_posicao
        while x >= posicao:
            self.valores[x + 1] = self.valores[x]
            x -= 1

        self.valores[posicao] = valor
        self.ultima_posicao += 1



vetor = VetorOrdenado(10)

vetor.insercao(5)
vetor.insercao(8)
vetor.insercao(9)
vetor.insercao(7)
vetor.insercao(2)

vetor.imprimir()




