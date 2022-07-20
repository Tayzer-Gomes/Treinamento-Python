#Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = float(input('Digite sua velocidade em Km/h:'))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('Você excedeu o limite de velocidade! Você foi MULTADO!')
    print('Sua multa custará {:.2f} R$.'.format(multa))
    print('Dirija com segurança! Tenha uma boa viagem!')

