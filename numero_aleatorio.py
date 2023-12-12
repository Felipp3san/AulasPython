import random

numero_aleatorio = random.randint(1, 6)

palpite = 0
tentativa = 0

while palpite != numero_aleatorio and tentativa < 3:

    valid_number = False
    while not valid_number:
        try:
            palpite = int(input("Tente adivinhar o numero sorteado entre 1 e 6: "))
            if 1 <= palpite <= 6:
                valid_number = True
            else:
                print("Apenas numeros entre 1 e 6 são válidos")
                valid_number = False
        except ValueError:
            print("Caracteres não são permitidos. Tente novamente.")

    if palpite == numero_aleatorio:
        print("Acertou, parabéns!")
    else:
        print("Numero errado, tente novamente.")
    tentativa = tentativa + 1
