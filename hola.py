import random
while True:
    print("introduce tu numero para adivinar")
    numero = int(input("numero: "))
    x = random.randint(0, numero)
    if numero != x:
        print("PERDISTE")
    else:
        print("GANASTE!!!!!!!!!!!!!!!!!!!!!!!")

