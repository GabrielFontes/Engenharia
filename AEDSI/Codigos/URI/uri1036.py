# coding: utf-8
from math import sqrt

valores = input().split()
A = float(valores[0])
B = float(valores[1])
C = float(valores[2])

delta = (B**2 - 4*A*C)

if delta >= 0 and A!=0:
    r1 = (- B + sqrt(delta))/ (2*A)
    r2 = (- B - sqrt(delta))/ (2*A)
    print("R1 = {:.5f}\nR2 = {:.5f}".format(r1, r2))

else:
    print("Impossivel calcular")
