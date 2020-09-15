# -*- coding: utf-8 -*-
valor = []
valor = input().split(".")
valor_notas = int(valor[0])
valor_moedas = int(valor[1])
notas = [100, 50, 20, 10, 5, 2]
moedas = [50, 25, 10, 5, 1]
i=0

print("NOTAS:")

for n in notas:
    while valor_notas>=n:
        valor_notas = valor_notas - n
        i+=1
    print("{} nota(s) de R$ {:.2f}".format(i, n))
    i=0

while valor_notas!=0 :
    valor_notas = valor_notas - 1
    i+=1

print("MOEDAS:")
print("{} moeda(s) de R$ 1.00".format(i))
i=0


for n in moedas:
    while valor_moedas>=n :
        valor_moedas = valor_moedas - n
        i+=1
    if n>=10:
        print("{} moeda(s) de R$ 0.{}".format(i,n))
    else:
        if n==1:
            while valor_moedas!=0:
                valor_notas = valor_notas - 1
                i+=1
        print("{} moeda(s) de R$ 0.0{}".format(i, n))
    i=0

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''