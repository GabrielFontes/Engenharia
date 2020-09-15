# coding: utf-8

produtos=input().split()
codigo = int(produtos[0])
quantidade = int(produtos[1])

if codigo==1:
    valor = quantidade * 4
elif codigo==2:
    valor = quantidade * 4.5
elif codigo==3:
    valor = quantidade * 5
elif codigo==4:
    valor = quantidade * 2
elif codigo==5:
    valor = quantidade * 1.5

print("Total: R$ {:.2f}".format(float(valor)))