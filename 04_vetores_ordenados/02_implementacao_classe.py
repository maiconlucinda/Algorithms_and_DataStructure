
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
    # Big-O = O(n)
    def pesquisa(self, valor):
        for i in range(self.ultima_posicao + 1):
            if self.valores[i] > valor | i == self.ultima_posicao:
                return -1
            if self.valores[i] == valor:
                return i


    #1 -  Validar se a estrutura já está cheia.
    #2 -  Encontrar posicao onde o elemento deverá ser adicionado
    #3 -  Movendo uma posicao a frente, todos os elementos presentes no vetor
    #4 -  Adicionar o novo valor na posicao correta do vetor
    # Big-O = O(n)
    def insercao(self, valor):
        #1
        if self.ultima_posicao == self.capacidade - 1:
            print('Capacidade máxima atingida')

        #2
        posicao = 0
        for i in range(self.ultima_posicao +1):
            posicao = i
            if self.valores[i] > valor:
                break
            if i == self.ultima_posicao:
                posicao = i + 1

        #3
        x = self.ultima_posicao
        while x >= posicao:
            self.valores[x + 1] = self.valores[x]
            x -= 1

        #4
        self.valores[posicao] = valor
        self.ultima_posicao += 1


    #1 - Verificar se o valor existe dentro do vetor, caso não encontre, retorne somente uma mensagem
    #2 - Caso exista o valor, tendo em mente sua posição, posso mover os elementos que estão a frente uma casa a esquerda
    #3 - Decrementar o tamanho do vetor
    def exclusao(self, valor):
        posicao = self.pesquisa(valor)
        if posicao == -1:
            return -1
        else:
            for i in range(posicao, self.ultima_posicao):
                self.valores[i] = self.ultima_posicao[i + 1]
            self.ultima_posicao -= 1



vetor = VetorOrdenado(10)

vetor.insercao(5)
vetor.insercao(8)
vetor.insercao(6)
vetor.insercao(7)
vetor.insercao(2)
print(vetor.pesquisa(8))
vetor.exclusao(8)

vetor.imprimir()




