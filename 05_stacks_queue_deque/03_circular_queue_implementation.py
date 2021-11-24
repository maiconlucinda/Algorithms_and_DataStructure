
import numpy as np

class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.beginning = 0
        self.end = -1
        self.number_elements = 0
        self.values = np.empty(self.capacity, dtype=int)


    def __empty_stack(self):
        # Operação boleana que vai retornar True ou False
        return self.number_elements == 0


    def __full_stack(self):
        # Operação boleana que vai retornar True ou False
        return self.number_elements == self.capacity


    def toqueue(self, value):
        if self.__full_stack():
            print('A fila está cheia')
            return

        if self.end == self.capacity - 1:
            self.end = -1
        self.end += 1
        self.values[self.end] = value
        self.number_elements += 1


    def unline(self):
        if self.__empty_stack():
            print('A fila está vazia')
            return

        # Variável para retornar qual elemento foi desenfileirado
        temp = self.values[self.beginning]
        self.beginning += 1
        if self.beginning == self.capacity - 1:
            self.beginning = 0
        self.number_elements -= 1
        return temp


    def first(self):
        if self.__empty_stack():
            return -1
        return self.values[self.beginning]



queue = CircularQueue(5)
#print(queue.first())

queue.toqueue(1)
queue.toqueue(2)
queue.toqueue(3)
queue.toqueue(4)
queue.toqueue(5)


queue.unline()
queue.unline()

queue.toqueue(6)
queue.toqueue(7)
print(queue.first())

print(queue.beginning, queue.end)
print(queue.values)

































