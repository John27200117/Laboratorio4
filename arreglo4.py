def suma(vector):
    for i in range(len(vector)):
        if (vector[i] == sum(vector[:i] + vector[i+1:])):
            return True
    return False
vector = [1,2,3,4,5,6,7,8,9,10]
print(suma(vector))

