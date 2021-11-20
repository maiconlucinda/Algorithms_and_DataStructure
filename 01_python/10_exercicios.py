
# 1 - Ler 5 notas e informar a média

soma = 0
for _ in range(1, 6):
    notaInserida = float(input('Insira as notas na Sequencia '))
    soma = soma + notaInserida
media = soma / 5
print(media,'\n')



#2 - Imprimir a tabuada do número 3 (3 x 1 = 1 - 3 x 10 = 30)
numero = 0
while numero < 11:
    resultado = numero * 3
    print(f"3 x {numero} = {resultado}")
    numero += 1
