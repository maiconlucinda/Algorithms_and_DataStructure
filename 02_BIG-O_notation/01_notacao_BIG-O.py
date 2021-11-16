
# O QUE É NOTAÇÃO BIG-O?
    # Como comparar dois algoritmos desenvolvidos por diferentes programadores?
    # Comparação objetiva entre algoritmos (não leva em conta sismema, nem linguagem... somente o algoritmo em si)
    # Considera diferenças entre poder de processamento, sistema operacional,linguagem de programação
    # O quanto a "complexidade" do algoritmo aumento de acordo com as entradas.


# Função 1

import timeit
def soma1(n):
    soma = 0
    for i in range(n + 1):
        soma += i
    return soma
print(soma1(10))


# Usando o recurso %timeit é possível saber a quantidade de ações que uma determinada função precisa executar
# para ser finalizada, caso seja realizada 9 ações por exemplo, podemos dizer que a função tem o BIG-O = 9.

# Isso é muito usado em situações que estamos desenvolvendo algum algorítmo e desejamos fazer comparação para
# ver a performance de nosso código.



