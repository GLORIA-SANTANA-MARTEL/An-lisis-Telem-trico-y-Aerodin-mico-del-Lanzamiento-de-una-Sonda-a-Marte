from scipy.linalg import lu_factor, lu_solve
from numpy import dot, linalg, array, zeros
from operator import matmul
import numpy as np
from numpy.linalg import cond
from fichero_matematico import my_jacobi, my_Gauss, my_LU

A = array([[1, 1, 1], 
           [1, 1, -1], 
           [1, -2, 0]])

b = array([50000, 15000, 0])

solucion = my_LU(A, b)

print(solucion)
