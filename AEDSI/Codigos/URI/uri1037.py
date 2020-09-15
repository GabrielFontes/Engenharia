# coding: utf-8

A = float(input())

if A>=0.0 and A<=25.00:
    print("Intervalo [0,25]")
elif A>25.0 and A<=50.0:
    print("Intervalo (25,50]")
elif A>50.0 and A<=75.0:
    print("Intervalo (50,75]")
elif A>75.0 and A<=100.0:
    print("Intervalo (75,100]")
else:
    print("Fora de intervalo")