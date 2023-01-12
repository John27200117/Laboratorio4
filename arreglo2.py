notas = [20, 15, 12, 11, 8, 4, 1]
B = []
maxN = 20
minN = maxN
for i in notas:
    if i < minN:
        minN = i
print("El promedio más bajo es: ",minN)
notas.remove(minN)
print(notas)
suma = 0
for j in notas:
    suma+= j
print(suma)
print("El promedio total es: ", suma/len(notas))
