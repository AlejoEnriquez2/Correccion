# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 09:42:23 2020

@author: alejo
"""
import numpy as np
from multiprocessing import Manager, Process
import multiprocessing
from MetodosMultiprocessing import Metodo1
import random
import time

# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 09:48:56 2020

@author: alejo
"""

import time

import random

import functools

from mpi4py import MPI
import numpy as np
 
num_procesos = 5    


def normalize_vector_sequential(ar):

    result = []

    squared_sum = 0

    for n in ar:

        squared_sum += n * n

    raiz = squared_sum**(.5)

   

    for n in ar:

        result.append(n/raiz)
        
    result.sort()
    #print(result)
    return result

 

# Complete the normalize_vector_parallel function below.

def normalize_vector_parallel(ar, squared_sum2):

    lista1 = []
    procesos = []

    procesos = multiprocessing.Pool(processes=4)
    
    lista1 = procesos.starmap(Metodo1, [(ar, squared_sum2)])[0]
    
    lista1.sort()
    #print(lista1)
    return lista1

 

if __name__ == '__main__':
    # Prepare data

    ar_count = 4000000

    #Generate ar_count random numbers between 1 and 30
    squared_sum2 = 0
    ar = [random.randrange(1,30) for i in range(ar_count)]
    for n in ar:
        squared_sum2 += n * n
   

    inicioSec = time.time()

    resultsSec = []

    resultsSec = normalize_vector_sequential(ar)

    finSec =  time.time()

    # You can modify this to adapt to your code

    inicioPar = time.time()   

    resultsPar = []

    resultsPar = normalize_vector_parallel(ar, squared_sum2)

    finPar = time.time()   


    print('Results are correct!\n' if functools.reduce(lambda x, y : x and y, map(lambda p, q: p == q,resultsSec,resultsPar), True) else 'Results are incorrect!\n')

    print('Sequential Process took %.3f ms \n' % ((finSec - inicioSec)*1000))

    print('Parallel Process took %.3f ms \n' % ((finPar - inicioPar)*1000))

  


        