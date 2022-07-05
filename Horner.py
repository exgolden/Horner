import numpy as np
print("Este programa evalua polinomios")
Coeff=str(input("Ingrese los coeficienets del polinomio -incluidos los elementos cero-: an,an-1,...,a2,a1: "))
VAL=float(input("Ingrese el valor a evaluar: "))
Coeff=np.array(Coeff.split(","), dtype=float)
K=Coeff[0]
for i in range(1, len(Coeff)):
    K=(K*VAL)+Coeff[i]
print("El polinomio evaluado en {VAL}, es igual a: {K}".format(VAL=VAL, K=K))
