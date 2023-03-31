import numpy as np
lista=[9,8,7,6,5,4,3,2,1,0]
def aritmeticka_sredina(lista):
    suma = 0
    n = len(lista)
    for i in range(n):
        suma+=lista[i]
    return suma/n
def sandardna_devijacija(lista):
    suma = 0
    n = len(lista)
    x_as=aritmeticka_sredina(lista)
    for i in range(n):
        suma+=(lista[i]-x_as)**2
    return np.sqrt(suma/(n*(n-1)))
print("Aritmetička sredina točaka iznosi {}".format(aritmeticka_sredina(lista)))
print("Standardna devijacija točaka iznosi {}".format(sandardna_devijacija(lista)))
#Koristeći np
print("Aritmetička sredina točaka iznosi {}".format(np.average(lista)))
print("Standardna devijacija točaka iznosi {}".format(np.std(lista)/3))