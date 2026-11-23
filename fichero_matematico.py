# MÉTODOS DE SOLUCIÓN DE SISTEMAS DE ECUACIONES LINEALES

### Librerías de importación
from scipy.linalg import lu_factor, lu_solve
from numpy import dot, norm, linalg, array, zeros, matmul, transpose
import numpy as np
from numpy.linalg import cond, solve

#1.RESOLUCION DE SISTEMAS LINEALES

## Directos

### Gauss

def  my_Gauss(A,b):

   N = len(b);  x = zeros(N)   
   for i in range(0, N): 
     pivoting_row_swapping( A, b, i, N)

     for k in range(i+1, N):  
       c = A[k,i] / A[i,i]  
       A[k,:] = A[k,:] - c * A[i,:] 
       b[k] = b[k] - c * b[i] 
     
   for i in range(N-1, -1, -1):
     x[i] = ( b[i] - dot( A[i,i+1:N], x[i+1:N] ) )/ A[i,i]

   return x 

#### Función de definición del pivote

def pivoting_row_swapping(A,b,k,N): 

     s = zeros(N)

     for i in range(k, N):   
       s[i] = max( abs(A[i,k:N]) ) 
      
     pivot = abs( A[k,k] / s[k] )
     l = k
     for j in range(k, N): 
       if abs( A[j,k] / s[j] ) > pivot: 
          pivot = abs( A[j,k] / s[j] )
          l = j

     if pivot == 0.0 :  print(" The matrix is singular "); exit()
       
     if l != k : 
        A[ [k, l] ,k:N] =  A[ [l, k], k:N]  
        ( b[k], b[l] ) =  ( b[l], b[k] )



### LU

def my_LU(A,b): 
  
  LU, piv = lu_factor(A)
  print("LU=", LU)
  print("pivot=", piv)

  x = lu_solve((LU, piv), b)
  print("x =", x, matmul(A,x)-b )
  return x





## Iterativos

### Jacobi

def my_jacobi(A,b): 

    N = len(b)
    x, D, R = zeros(N), zeros(N), zeros((N,N))
    xn = 1 + x 
    tolerance = 1e-10
    k, max_iter = 0, 100

  #### Jacobi iteration
    for i in range(N): 
     for  j in range(N): 
       if i==j: 
          D[i] = A[i,j]
          R[i,j] = 0 
       else:
          R[i,j] = A[i,j]
   
    while norm(xn - x) > tolerance  and  k < max_iter: 
        x = xn
        xn = (b - dot(R, x)) / D
      

    return x 


### Gauss Seidel

def Gauss_Seidel(A,b):

    N = len(b)
    x1, x2, b1 = zeros(N), zeros(N), zeros(N)
    Error, tolerance = 1, 1e-10 
    k, max_iter = 0, 100

  #### Gauss Seidel iteration
    while Error > tolerance  and  k < max_iter: 

        x1[:] = x2[:]   # x1=x2 does not work 
        for i in range(N):
            b1[i] = b[i] - dot( A[i, i+1:], x1[i+1:] )  # old values  

        for i in range(N):
            x2[i]  = ( b1[i] - dot( A[i, :i], x2[:i] ) )/ A[i, i] 
         
        Error = norm(x2-x1)
        k += 1

    return x2  

#2.REGRESION LINEAL

##VANDERMONDE
def Vandermonde(x, N, M): 
   
    return array( [  [ x[j]**i for i in range(N) ] for j in range(M) ] ) 

##REGRESSION VANDERMONDE
def regression_vandermonde(x, y, N): 

      M = len(x)
      A = Vandermonde(x, N, M) 
     
      return solve( matmul(transpose(A), A ), matmul(transpose(A), y) ) 

##POLINOMYAL
def polynomial(w, x): 

   N = len(w)
   return sum(   w[k] * x**k for k in range(N) )


#3.INTEGRACION NUMERICA 1D
#4.INTERPOLACION 1D
#5.DERIVACION NUMERICA 1D
#6.ECUACION NO LINEAL
