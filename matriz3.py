import numpy as np

A = np.array([[1,2,3,4],[5,6,7,8],[11,22,33,44],[55,66,77,88]])
print("Matriz A: ")
print(A)

print("La diagonal principal es: ")
B = []
for i in range(len(A)):
    for j in range(len(A[i])):
        if i == j:
            B.append(A[i][j])
print(B)

diagoPrincipal = 0
for i in range(len(A)):
    for j in range(len(A[i])):
        if i == j:
            diagoPrincipal = diagoPrincipal + A[i][j]
print("La suma de la diagonal principal es: ")
print(diagoPrincipal)
