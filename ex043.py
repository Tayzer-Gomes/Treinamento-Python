#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# IMC abaixo de 18,5: Abaixo do Peso
# Entre 18,5 e 25: Peso Ideal
# 25 até 30: Sobrepeso
# 30 até 40: Obesidade
# Acima de 40: Obesidade Mórbida
peso = float(input('Qual seu peso?'))
altura = float(input('Qual sua altura?'))
imc = peso / (altura * altura)
print('Seu imc é {:.2f}!'.format(imc))
if imc < 18.5:
    print('IMC abaixo de 18,5: Abaixo do Peso')
elif imc == 18.5 or imc < 25:
    print('Entre 18.5 e 25: Peso ideal.')
elif imc == 25 or imc < 30:
    print('Entre 25 até 30: Sobrepeso')
elif imc == 30 or imc < 40:
    print('Entre 30 até 40: Obesidade')
elif imc >= 40:
    print('Acima de 40: Obesidade Mórbida')

