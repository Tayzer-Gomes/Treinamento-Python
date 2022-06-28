#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = float(input('Digite um valor: '))
dobro = (n*2)
triplo = (n*3)
rq = (n**(1/2))
print('O número digitado foi {}, seu dobro equivale a {}, seu triplo é {} e sua raiz quadrada é {}!'.format(n, dobro, triplo, rq))
