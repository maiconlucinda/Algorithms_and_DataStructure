
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







# Time