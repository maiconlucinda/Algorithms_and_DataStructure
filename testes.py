
import numpy as np

class VetorOrdenado:


    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade, dtype=int)


    def pesquisa(self, valor):
        if self.ultima_posicao == -1:
            return self.ultima_posicao
        else:
            for i in range(self.ultima_posicao + 1):
                if valor == self.valores[i]:
                    return i
            return -1

vetor = VetorOrdenado(8)
print(vetor.pesquisa(3))