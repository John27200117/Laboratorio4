import numpy as np

A = np.array([[1,2],[3,4],[5,6]])
print("Matriz A: ")
print(A)
B = np.array([[1,2,3],[4,5,6]])
print("Matriz B: ")
print(B)

multiplicacion = np.dot(A,B)
print("La matriz resultado de A*B es: ")
print(multiplicacion)
