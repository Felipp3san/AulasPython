idade = input("Qual é a sua idade? ")

if int(idade) < 18:
    print("Menor de idade")
elif int(idade) > 70:
    print("Aposentadoria a vista")
else:
    print("Maior de idade")

################

nota = 30

if nota >= 70:
    print("Bom")
elif nota >= 50:
    print("Medio")
elif nota >= 30:
    print("Fraco")
else:
    print("Muito Fraco")

# Operadores lógicos

domingo_faz_sol = True
tenho_boleia = True
passe_valido = False

if domingo_faz_sol:
    if not tenho_boleia:
        if not passe_valido:
            print("Ir a pé")
        else:
            print("Pegar o onibus")
    else:
        print("Es folgado")
else:
    print("Ficar em casa mofando")

# Operadores de comparação
'''
 < menor
 > maior
 <= menor ou igual
 > maior ou igual
 == igual
 != diferente
'''

# PASSWORD

password = "abc8123"

if 6 < len(password) < 15:
    print("Password válido")
else:
    print("Password inválido")
