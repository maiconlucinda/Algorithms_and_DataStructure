
import numpy as np

class stack:

    def __init__(self, capacidade):
        self.__capacidade = capacidade
        self.__topo = -1
        self.__valores = np.empty(self.__capacidade, dtype=dtype)


    # Verify if the stack is full
    def __full_stack(self):
       if self.__topo == self.__capacidade - 1:
           return True
       else:
           return False


    # Verify is the stack is empty
    def __empty_stack(self):
        if self.__topo == -1:
            return True
        else:
            return False


    # Add a item in the stack
    def stackup(self, valor):
        if self.__full_stack():
            print('A pilha está cheia')
        else:
            self.__topo += 1
            self.__valores[self.__topo] = valor


    # Remove the last element from the stack
    def unstack(self):
        if self.__empty_stack():
            print('A pilha está vazia')
        else:
            self.__topo -= 1


    # Show the top of the stack
    def showtop(self):
        if self.__topo != -1:
            return self.__valores[self.__topo]
        else:
            return -1



stack = stack(5)

stack.stackup(7)
stack.stackup(3)
stack.stackup(4)
stack.stackup(1)

stack.unstack()
stack.unstack()

print(stack.showtop())

