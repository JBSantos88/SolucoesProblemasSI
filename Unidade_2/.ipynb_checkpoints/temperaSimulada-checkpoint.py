
"""

Algoritmo de Têmpera Simulada
Objetivo: encontrar o valor de x que maximiza a função:

                y = sen(1/x)/x 

"""

import math
import numpy

def vizinho(x):

    delta = numpy.random.uniform(-0.0001, 0.0001)
    x = x+delta

    if x < 0.01:
        x = 0.001
    if x > 1:
        x = 1
    return x

def valor(x):

    y = math.sin(1/x)/x
    return y


def initialState():
    return numpy.random.uniform(0.01,1)


def probabilidade(t, delta_e):

    p = math.exp(delta_e/t)
    return p

atual = initialState()
t = 700000
tmin = 1

while (t>tmin):

    t = 0.99999*t
    
    prox = vizinho(atual)
    delta_e = valor(prox) - valor(atual)

    if (delta_e>0):
        atual = prox
    else: 
        p = probabilidade(t,delta_e)
        if(numpy.random.uniform(0,1) < p):
            atual = prox

print("y = ",valor(atual))
print("x = ",prox)
