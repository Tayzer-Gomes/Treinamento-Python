#Escreva um programa que converta uma temperatura digitada em °C e converta para °F

n = float(input('Digite uma temperatura em °C: '))
c = (n * (9/5)) + 32
print('Sua temperatura em °C é {} e em Fahrenheit é {:.1f}'.format(n, c))
