import numpy as np

class ExpressionValidator:

    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.topo = -1
        self.valores = np.chararray(self.capacidade, unicode=True)


    # Verify if the stack is full (private method)
    def __full_stack(self):
        if self.topo == self.capacidade - 1:
            return True
        else:
            return False
    

    # Verify is the stack is empty (private method)
    def empty_stack(self):
        if self.topo == -1:
            return True
        else:
            return False


    # Adding a new value to the stack
    def stackup(self, valor):
        if self.__full_stack():
            print('The stack is full')
        else:
            self.topo += 1
            self.valores[self.topo] = valor


    # Removing a value from the stack 
    def unstack(self):
        if self.empty_stack():
            print('The stack is empty')
            return -1
        else:
            valor = self.valores[self.topo]
            self.topo -= 1
            return valor


    # Show the last value from the stack
    def show(self):
        if self.topo != -1:
            return self.valores[self.topo]
        else:
            return -1



expressao = str(input('Digite uma expressao: '))
pilha = ExpressionValidator(len(expressao))


for i in range(len(expressao)):

    ch = expressao[i] #Recebeu uma das letras da expessão
    if ch == '{' or ch == '[' or ch == '(':
        # Se o ch for {[(, adiciono na pilha.
        pilha.stackup(ch)

    elif ch == '}' or ch == ']' or ch == ')':

        if not pilha.empty_stack():
            chx = str(pilha.unstack())
            if (ch == '}' and chx != '{') or (ch == ']' and chx != '[') or (ch == '(' and chx != '('):
                print('Erro: ', ch, ' na posição ', i)
                break

        else:
            print('Erro: ', ch, ' na posição', i)


if not pilha.empty_stack():
    print('Erro!')



    
#validator = ExpressionValidator(50)

#validator.stackup('Hello World')
#validator.stackup('My name is Maicon')

#print(validator.show())

    
