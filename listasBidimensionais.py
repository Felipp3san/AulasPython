matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(matriz)
print(matriz[0])
print(matriz[0][2])

for linha in range(len(matriz)):
    for coluna in range(len(matriz[linha])):
        print(matriz[linha][coluna])


for row in matriz:
    for elem in row:
        print(elem)

