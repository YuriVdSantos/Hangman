import pyttsx3

fala = pyttsx3.init()

fala.say("Olá humano, bem-vido ao jogo da Forca! Por favor, digite a palavra que você deseja adivinhar"
", mas sem que seus amiguinhos vejam")
fala.runAndWait()

palavra = input("Digite a palavra: ")
lista_palavra = list(palavra)
acertadas = []
erros = 0
acertou = False

fala.say("Agora espere seus amiguinhos adivinhar a palavra, ou errar kkkkkk")
fala.runAndWait()

print("Fica a dica a palavra tem {} letras".format(len(palavra)))

for i in range(0, len(palavra)):
    lista_palavra.append("*")


while acertou == False:
    letra = str(input("Digite uma letra: "))

    for i in range(0, len(lista_palavra)):
        if letra == lista_palavra[i]:
            acertadas[i] = letra
        
        print(acertadas[i])
    
    acertou = True
    

    for x in range(0, len(acertadas)):
        if acertadas[x] == "*":
            acertou = False
            break
        


'''
while erros <5:
    letra = input("Digite uma letra: ")
    if letra in palavra:
        print("A letra {} está na palavra".format(letra))
    else:
        print("A letra {} não está na palavra".format(letra))
        erros += 1
        print("Você tem {} erros".format(erros))
        if erros == 5:
            print("Você perdeu")
            fala.say("Você perdeu")
            fala.runAndWait()
            break
'''