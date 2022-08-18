# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#EQUILÁTERO: todos os lados iguais
#ISÓSCELES: dois lados iguais, um diferente
#ESCALENO: todos os lados diferentes


ladoA = float(input('Digite o comprimento da reta 1:'))
ladoB = float(input('Digite o comprimento da reta 2:'))
ladoC = float(input('Digite o comprimento da reta 3:'))
if ladoA < ladoB + ladoC and ladoB < ladoA + ladoC and ladoC < ladoA + ladoB:
    print('As retas acima podem formar um triângulo.')
    if ladoA == ladoB == ladoC:
        print('Suas retas formam um triângulo EQUILÁTERO.')
    elif ladoA != ladoB != ladoC != ladoA:
        print('Suas retas formam um triângulo ESCALENO.')
    else:
        print('Suas retas fromam um triângulo ISÓSCELES.')
else:
    print('As retas não podem formar um triângulo.')