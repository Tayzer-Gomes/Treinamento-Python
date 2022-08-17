#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
#Média abaixo de 5.0: REPROVADO
#Média entre 5.0 e 6.9: RECUPERAÇÃO
#Média 7.0 ou superior: APROVADO


nota1 = float(input('Digite sua primeira nota:'))
nota2 = float(input('Digite sua segunda nota:'))
media = (nota1 + nota2) / 2
print('Sua média é {:.2f}'.format(media))
if media > 10.0:
    print('Sua média máxima é 10. Tente novamente!')
elif media < 5:
    print('Média abaixo de 5.0: REPROVADO.')
elif media == 5 or media <= 6.9:
    print('Média entre 5.0 e 6.9: RECUPERAÇÃO.')
elif media >= 7.0 or media <=10.0:
    print('Média 7.0 ou superior: APROVADO.')

