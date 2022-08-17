#Faça um programa que leia o ano de nascimento de um jovem e informe,
# de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
# se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
anoAtual = date.today().year
ano = int(input('Qual o ano de seu nascimento:'))
idade = anoAtual - ano
tempoRestante = 18 - idade
tempoUltrapassado = idade - 18
if (idade < 18):
        print('Falta {} anos para seu alistamento. Você ainda vai se alistar!'.format(tempoRestante))
elif (idade == 18):
        print('Está na hora de você se alistar!')
elif(idade > 18):
        print('Seu tempo para o alistamento ultrapassou {} anos. Você passou da hora de alistar!'.format(tempoUltrapassado))



