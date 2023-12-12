import numpy as np

idade = [10, 15, 20, 25, 30, 35, 40]
print(idade)

nome = ["Marcos", "Pedro", "Joao", "Joana", "Rita"]
print(nome)  # Escreve o array completo
print(nome[1])  # Escreve o elemento presente na posição 2 do array
print(nome[2:])  # Começa da posição 2 e vai até o final do array
print(nome[1:3])  # Começa da posição 1 e vai até a posição 3 (não inclusive)
print(nome[2][0])  # Escreve o primeiro caractere do 3 elemento do array

nome.append("Felippe")  # Adiciona novos elemento no final do array
print(nome)

# Encontrar o maior numero

# forma comum
numeros = [5, 3, 7, 19, 1, 3, 4, 12, 6, 7]

maior = numeros[0]
for numero in numeros:
    if numero > maior:
        maior = numero

print(maior)

# utilizando numpy.max
maior_np = np.max(numeros)
print(maior_np)
