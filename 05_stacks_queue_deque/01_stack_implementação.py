
import numpy as np

class stack:

    def __init__(self, capacidade):
        self.__capacidade = capacidade
        self.__topo = -1
        self.__valores = np.empty(self.__capacidade, dtype=int)


    def __full_stack(self):
       if self.__topo == self.__capacidade - 1:
           return True
       else:
           return False


    def __empty_stack(self):
        if self.__topo == -1:
            return True
        else:
            return False

    def stackup(self, valor):
        if self.__full_stack():
            print('A pilha está cheia')
        else:
            self.__topo += 1
            self.__valores[self.__topo] = valor


    def unstack(self):
        if self.__empty_stack():
            print('A pilha está vazia')
        else:
            self.__topo -= 1


    def showtop(self):
        if self.__topo != -1:
            return self.__valores[self.__topo]
        else:
            return -1



stack = stack(5)
stack.stackup(7)
print(stack.showtop())

