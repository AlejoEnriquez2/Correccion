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
 

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
procesos = comm.Get_size()

numworkers = procesos - 1

def normalize_vector_sequential(ar):

    result = []

    squared_sum = 0

    for n in ar:

        squared_sum += n * n

    raiz = squared_sum**(.5)

   

    for n in ar:

        result.append(n/raiz)

    return result

 

# Complete the normalize_vector_parallel function below.

def normalize_vector_parallel(ar):

    #implement you solution
    

    res = [0]

    return res

 

if __name__ == '__main__':

   

    # Prepare data

    ar_count = 4000000

    #Generate ar_count random numbers between 1 and 30

    ar = [random.randrange(1,30) for i in range(ar_count)]

   

    inicioSec = time.time()

    resultsSec = []

    resultsSec = normalize_vector_sequential(ar)

    finSec =  time.time()

   

    # You can modify this to adapt to your code

    inicioPar = time.time()   

    resultsPar = []

    resultsPar = normalize_vector_parallel(ar)

    finPar = time.time()   

   

    print('Results are correct!\n' if functools.reduce(lambda x, y : x and y, map(lambda p, q: p == q,resultsSec,resultsPar), True) else 'Results are incorrect!\n')

    print('Sequential Process took %.3f ms \n' % ((finSec - inicioSec)*1000), ", ", resultsSec)

    print('Parallel Process took %.3f ms \n' % ((finPar - inicioPar)*1000))

  