import numpy as np

class ExpressionValidator:

    def __init__(self, capacidade) -> None:
        self.__capacidade = capacidade
        self.__topo = -1
        self.__valores = np.chararray(self.__capacidade, unicode=True)


    # Verify if the stack is full (private method)
    def __full_stack(self):
        if self.__topo == self.__capacidade -1:
            return True
        else:
            return False
    

    # Verify is the stack is empty (private method)
    def empty_stack(self):
        if self.__topo == -1:
            return True
        else:
            return False


    # Adding a new value to the stack
    def stackup(self, valor):
        if self.__full_stack():
            print('The stack is full')
        else:
            self.__topo += 1
            self.__valores[self.__topo] = valor
            print(self.__valores)


    # Removing a value from the stack 
    def remove(self):
        if self.__empty_stack():
            print('The stack is empty')
            return -1
        else:
            valor = self.valores[self.__topo]
            self.__topo -= 1
            return valor


    # Show the last value from the stack
    def show(self):
        if self.__topo != -1:
            return self.__valores[self.__topo]
        else:
            return -1





    
#validator = ExpressionValidator(50)

#validator.stackup('Hello World')
#validator.stackup('My name is Maicon')

#print(validator.show())

    
