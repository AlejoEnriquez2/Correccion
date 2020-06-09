# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 09:43:58 2020

@author: alejo
"""

from mpi4py import MPI
import numpy as np
import time
import random
import functools

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
procesos = comm.Get_size()


def normalize_vector_sequential(ar):

    result = []

    squared_sum = 0

    for n in ar:

        squared_sum += n * n

    raiz = squared_sum**(.5)

   

    for n in ar:

        result.append(n/raiz)
        
    result.sort()
    return result

 

# Prepare data
ar_count = 4000000
#Generate ar_count random numbers between 1 and 30
squared_sum = 0

numworkers = procesos - 1
resultado = []
result = []

if rank==0:    
    datos = [random.randrange(1,30) for i in range(ar_count)]
    for n in datos:
        squared_sum += n * n
        
    datosCant=ar_count
    inicioSec = time.time()
    resultsSec = []
    resultsSec = normalize_vector_sequential(datos)
    finSec =  time.time() 
    p = datosCant//numworkers
    residuo = datosCant % numworkers
    inicio = 0
    ti = time.time()
    
    for i in range(1, procesos):
        extra = p+1 if i <= residuo else p
        comm.send(datos[inicio:inicio+extra], dest=i, tag=1)
        comm.send(squared_sum, dest=i, tag=2)
        inicio = inicio + extra
        #tiempos = tiempos + tiempoRes
    
    for i in range(1, procesos):
        res= comm.recv(source=i, tag=1)
        resultado.extend(res)
        
        
    tf = time.time()
    tt = (tf-ti)*1000
    #print("Tiempo MPI: ", tt, "Resultado: ", resultado)
    
    resultado.sort()
    
    print('Results are correct!\n' if functools.reduce(lambda x, y : x and y, map(lambda p, q: p == q,resultsSec,resultado), True) else 'Results are incorrect!\n')
    print('Sequential Process took %.3f ms \n' % ((finSec - inicioSec)*1000))
    print('Parallel Process took %.3f ms \n' % tt)
    

if rank > 0:
    a = comm.recv(source=0, tag=1)
    squared_sum = comm.recv(source=0, tag=2)

    raiz = squared_sum**(.5)
    
    for n in a:
        result.append(n/raiz)
    
    comm.send(result, dest=0, tag=1)
   

 



    

        
        
    
    
    
