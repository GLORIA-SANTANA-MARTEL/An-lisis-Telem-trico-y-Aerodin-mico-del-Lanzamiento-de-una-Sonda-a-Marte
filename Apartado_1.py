from numpy import array
from fichero_matematico import my_Jacobi, my_Gauss, my_LU, my_GaussSeidel

A = array([[1, 1, 1], 
           [1, 1, -1], 
           [1, -2, 0]])

b = array([50000, 15000, 0])

Gauss = my_Gauss(A, b)
LU = my_LU(A, b)
Jacobi = my_Jacobi(A, b)
GaussSeidel = my_GaussSeidel(A, b)

print("Solución por Gauss:", Gauss)
print("Solución por LU:", LU)
print("Solución por Jacobi:", Jacobi)
print("Solución por Gauss-Seidel:", GaussSeidel)
