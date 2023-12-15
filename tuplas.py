lista = []  # Mutáveis
tupla = ()  # Imutáveis

num1 = [1, 2, 3]
num2 = (1, 2, 3)

num1[0] = 5
# num2[0] = 5  # Não funciona (é tupla)

print(num1)
print(num2)

aluno = {'nome': 'Joana'}
print(aluno)
print(aluno['nome'])
