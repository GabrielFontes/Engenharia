# coding UTF-8

def divisores():
    linhas=input()
    valor=input()
    for k in range(linhas):
        j=1
        for i in range(1,valor//2):
            if valor%i == 0:
                j+=1
