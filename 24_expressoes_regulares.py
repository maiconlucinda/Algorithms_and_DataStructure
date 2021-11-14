
# EXPRESSÕES REGULARES

# O que são Expressões Regulares?

# Busca sofisticada por padrões

# Procurar todas as palavras que começam com letra minúscula, ou que começam com letra maiúscula e termina
# com letra minúscula...

# Palavras que comemçam com 'a' e terminam com 'e'

# Posso buscar qualquer tipo de padrão que ocorre em um tempo

# Os padrões de busca são praticamente ilimitados




# QUANDO TRABALHAMOS COM EXPRESSÕES REGULARES, TEMOS BASICAMENTE 3 MÉTODOS (FUNÇÕES)
    # Primeiro método: Search (significa encontrar ou pesquisar) - A ideia é encontrar padrões de Strings se estiverem presentes
    # Segundo método: Match - Encontrar se o começo de uma string é igual a um determinado padrão.
    # Terceiro método: Findall - Encontrar todas as substrings em uma strings que correspondam a um padrão.




# TRABALHANDO COM EXPRESSÕES REGULARES, TEMOS TAMBÉM OS METACARACTERES
    # . - Qualquer caractere (exceto linha noba)
    # \w - Qualquer caractere alfanumérico
    # \W - Qualquer caractere não-alfanumérico
    # \d - Qualquer caractere que seja um digito (0-9)
    # \D - Qualquer caractere não digito
    # \s - Espaço em branco
    # ˆ  - A palavra deve começar com uma determinada letra
    # $  - A palavra deve terminar com uma determinada letra
    # "\" - Usado antes de metacaracteres para especificar seu significado literal.




# TEMOS TAMBÉM OS QUANTIFICADORES - PERMITE DETERMINAR COMO E QUANTAS VEZES OS METACARACTERES APARECEM
    # [] - Opcional entre os que estão dentro dos colchetes (pode ter determinada letra ou não)
    # () - Captura grupos de caracteres.
    # *  - Significa que a letra pode aparecer de ZERO ou MAIS VEZES.
    # ?  - Significa que uma determinada letra pode aparecer ZERO ou UMA VEZ
    # +  - Significa que determinada letra pode aparecer UMA ou mais VEZES (esse padrão obrigatoriamente precisa aparecer pelo menos uma vez)
    # {m,n} - de M a N vezes (posso falar quantas vezes)
    # |  - Significa OU



