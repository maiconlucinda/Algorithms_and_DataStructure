
# importar tudos os módulos que serão necessário utilizar
import numpy as np

class OrderdedVector:


    # O primeiro método precisa ser o construtor, esse irá definir as propriedades para o escopo.
    # Irá também criar a estrutura necessária
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        # Não posso criar a estrutura me baseando no valor capacidades, pois ele será alterado por outros métodos também
        self.valores = np.empty(self.capacidade, dtype=int)


    def show(self):
        if self.ultima_posicao == -1:
            print('O vetor está vazio')
        else:
            for i in range(self.ultima_posicao + 1):
                print(i, '-', self.valores[i])


    # 1 - Caso o valor do última posição seja igual a -1, posso retornar -1, para dizer que não existe ese valor dentro.
    # 2 - Loop para buscar até a última posição, algum valore que corresponda ao valor procurado
    # 3 - Caso o valor seja encontrado, retorne a posição do mesmo.
    # O(n)
    def linear_search(self, valor):
        for i in range(self.ultima_posicao + 1):
            if self.valores[i] > valor | i == self.ultima_posicao:
                return -1
            if self.valores[i] == valor:
                return i
        return -1


    # 0(log n)
    def binary_search(self, valor):
        limite_inferior = 0
        limite_superior = self.ultima_posicao

        while True:
            posicao_atual = int((limite_inferior + limite_superior) / 2)

            # Se achou na primeira tentativa
            if self.valores[posicao_atual] == valor:
                return posicao_atual

            # Se não encontrou o valor (encera o loop)
            elif limite_inferior > limite_superior:
                return -1

            # Diminuindo o alcance
            else:
                # Alcance será a parte da esquerda (inferior)
                if self.valores[posicao_atual] < valor:
                    limite_inferior = posicao_atual + 1

                # Alcance será a parte da direita (superior)
                else:
                    limite_superior = posicao_atual - 1


    #1 -  Validar se a estrutura já está cheia.
    #2 -  Encontrar posicao onde o elemento deverá ser adicionado
    #3 -  Movendo uma posicao a frente, todos os elementos presentes no vetor
    #4 -  Adicionar o novo valor na posicao correta do vetor
    # Big-O = O(n)
    def insert(self, valor):
        #1
        # Por que -1? Porque no Python o indice comeca no zero, então de zero até 9 temos 10 posições.
        if self.ultima_posicao == self.capacidade - 1:
            print(f'Não foi possível adicionar o valor {valor}, capacidade máxima atingida')
            return

        #2
        posicao = 0
        # Por que +1? Porque o range se inicia com -1, então o +1 irá fazer com que chegue no zero. E depois sempre irá um número a frente do necessário
        for i in range(self.ultima_posicao +1):
            if self.valores[i] == valor:
                print(f'The value {valor} already exists in the vector')
                return -1
            else:
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
    def delete(self, valor):
        posicao = self.linear_search(valor)
        if posicao == -1:
            return -1
        else:
            print(range(posicao, self.ultima_posicao))
            for i in range(posicao, self.ultima_posicao):
                self.valores[i] = self.valores[i + 1]
            self.ultima_posicao -= 1



vector = OrderdedVector(10)

vector.insert(10)
vector.insert(9)
vector.insert(8)
vector.insert(7)
vector.insert(6)
vector.insert(5)
vector.insert(4)
vector.insert(3)
vector.insert(2)
vector.insert(1)
print(vector.binary_search(3))
#vector.delete(5)
vector.show()




