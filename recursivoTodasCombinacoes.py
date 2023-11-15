# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 07:12:01 2023

@author: ASGUNZI
"""
import numpy as np

list1 = [1, 2, 3]

outRespostas = []
isEnd = False

def geraCombinacoes(lstRef, posicao, vecSaida):
    global isEnd
    global outRespostas
    
    if posicao<len(lstRef):
        for i in range(len(lstRef)):
            vecSaida2 =vecSaida.copy()
            vecSaida2[posicao] = lstRef[i]
            geraCombinacoes(lstRef, posicao+1, vecSaida2)
    else:
        outRespostas.append(list(vecSaida))
            


vecSaida0 = np.zeros(len(list1), dtype = int)
geraCombinacoes(list1, 0, vecSaida0)

print(outRespostas)


        