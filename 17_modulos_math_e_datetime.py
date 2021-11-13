
# Alguns módulos úteis para quando estamos desenvolvendo algum tipo de aplicativo

# BIBLIOTECAS

# Math
import math

# Função para tirar raíz quadrada
print(math.sqrt(9))

# Função para calcular seno
print(math.sin(45))

# Função para calcular o coseno
print(math.cos(45))

# Função para extrair logarítmos de um número. EX: 100 na base 10. Simplesmente um número que eu multiplicaria a base (10) para chegar até o 100.
print(math.log(100, 10))

# Função para extrair logarítmos
print(math.log(32, 2))

# Função para extrair logarítmos (quando não insiro o valor base, será usado o número de Euler que é 2.71...)
print(math.log(1000))

# Pegar valor de pi
print(math.pi)
print('\n')




# Datetime
import datetime

# Ter acesso as opções de valores e funções que existem ao utilizarmos essa biblioteca
print(dir(datetime))

# Ver a data de hoje
print(datetime.date.today())

# Ver a hora atual
print(datetime.datetime.now())

# Criando variável com valores de dia, mes e ano
date = datetime.datetime(2021, 11, 13)
print(date.day)
print(date.month)
print(date.year)

# Criando variável com valores de horas
horario = datetime.datetime(2021, 11, 13, 6, 3, 0)
print(horario.hour)
print(horario.minute)
print(horario.second)
print('\n')




# Random
import random

# Função para gerar número randomicos
print(random.random())

# Função para gerar números randomicos dentro de uma determinada faixa
print(random.randint(1, 5))

# Função para gerar número randomicos dentro de uma determinada faixa com o passo step (terceiro argumento definido)
print(random.randrange(0, 10, 2)) # Nesse caso teremos somente números pares e o número 0

# Função para gerar número randomicos dentro de uma determinada faixa com o passo step
print(random.randrange(0, 10, 3)) # Nesse caso teremos somente números impares e o número 0

# Criando uma lista e depois realizando sorteio de um dos elementos
x = ['k', 'd', 13, '34-j', 'x']
print(x)
print(random.choice(x))
print('\n')



# Time
import time as tm

# Função para retornar o temp atual em segundos
print(tm.time())

# Função para testar a quantidade de tempo que um código levou para processar
antes = tm.time()
lista = []
for i in range(0,10000):
    lista.append(i)
depois = tm.time()
intervalo = depois - antes
print(f'Tempo: {intervalo} segundos')

# Função para parar a execução por um determinado - Função excelente para mandar mensagem para o usuário.
print('Finanlizando')
tm.sleep(2)
print('...')
tm.sleep(2)
print('Até a próxima')