# 2 Leia a idade do usuário e classifique-o em:
# - Criança – 0 a 12 anos
# - Adolescente – 13 a 17 anos
# - Adulto – acima de 18 anos
# -Se o usuário digitar um número negativo, mostrar a mensagem que a idade é inválida

idade_do_usuario = int(input('Enter your age '))

if (idade_do_usuario >= 0) & (idade_do_usuario <= 12):
    print('You are classified as a child')
elif (idade_do_usuario > 12) & (idade_do_usuario <= 18):
    print('You are classified as a teenager')
elif idade_do_usuario > 18:
    print('You are adult')
else:
    print('Invalid Age')
print('\n')





# 2 Calcular a média de um aluno que cursou a disciplina de Programação I, a partir da leitura das notas M1, M2 e M3;
# passando por um cálculo da média aritmética. Após a média calculada, devemos anunciar se o aluno foi aprovado, reprovado ou pegou exame
# - Se a média estiver entre 0.0 e 4.0, o aluno está reprovado
# - Se a média estiver entre 4.1 e 6.0, o aluno pegou exame
# - Se a média for maior do que 6.0, o aluno está aprovado
# - Se o aluno pegou exame, deve ser lida a nota do exame. Se a nota do exame for maior do que 6.0, está aprovado, senão; está reprovado

gradeM1 = float(input('Enter your M1 grade '))
gradeM2 = float(input('Enter your M2 grade '))
gradeM3 = float(input('Enter your M3 grade '))

gradeAverage = (gradeM1 + gradeM2 + gradeM3) / 3


if (gradeAverage >= 0) and (gradeAverage <= 4.0):
    print('Failed student')
elif (gradeAverage >= 4.1) and (gradeAverage <= 6.0):
    exam = float(input('Digite a nota do exame '))
    if exam >= 6.0:
        print('Aprovado no exame')
    else:
        print('Reprovado no exame')
else:
    print('Aluno aprovado')












