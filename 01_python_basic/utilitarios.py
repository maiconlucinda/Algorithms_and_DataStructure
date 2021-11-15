
def soma(a,b,c):
    somatorio = a+b+c
    return somatorio

def mult(a,b,c):
    produto = a*b*c
    return produto

def isPalindromo(string):
    if string == string[::-1]: # No python ::-1 significa que o valor será colocado de trás pra frente.
        return True
    else:
        return False

def divisao(a,b):
    return a/b

