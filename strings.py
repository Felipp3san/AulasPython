# String

frase = "Hoje está sol"
print(frase)  # escreve a frase inteira no console
print(frase[0])  # escreve o primeiro char da frase
print(frase[0:6])  # escreve do inicio até o 6 caractere
print(frase[:6])  # faz o mesmo de cima
print(frase[7:])  # começa do 7 caractere e vai até o final
print(frase[-2])  # escreve o penultimo caractere
print(frase[::-1])  # escreve a frase ao contrário
print(frase[::-2])  # escreve a frase ao contrário de 2 em 2

# Percorrer os caracteres da frase
print("========")

tamanho_frase = int(len(frase) / 2)
j = tamanho_frase

for i in range(0, len(frase)):
    if i >= tamanho_frase:
        print("\t" * j + frase[i])
        j = j - 1
    else:
        print("\t" * i + frase[i])

# String formatada

nome = "Felippe"
apelido = "Santana"
idade = 29

print("")
# O Felippe Santana tem 29 anos.
frase = "O " + nome + " " + apelido + " tem " + str(idade) + " anos."
print(frase)
frase = f"O {nome} {apelido} tem {str(idade)} anos."
print(frase)

# Métodos String

nome = "Felippe Santana"
print(len(nome))  # retorna o tamanho da string
print(nome.upper())  # escreve o nome com letras maiúsculas
print(nome.lower())  # escreve o nome com letras minúsculas
print(nome.find('i'))  # encontra a posição da primeira ocorrência do caractere indicado. retorna -1 se não encontrar
print(nome.find('tan'))  # encontra a posição onde começa a substring. retorna -1 se não encontrar

contem = "Felippe" in nome  # verifica se a frase contem a string indicada
print(contem)
