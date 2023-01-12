A = int(input("Ingrese el tamaño del arreglo: "))
B = []
C = []
for i in range(0,A):
    B.append(input("Ingrese nombre de las personas: "))
print(B)
for j in range(0,A):
    C.append(len(B[j]))
print(C)
