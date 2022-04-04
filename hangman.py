import pyttsx3

fala = pyttsx3.init()

fala.say("Olá humano, bem-vido ao jogo da Forca! Por favor, digite a palavra que você deseja adivinhar"
", mas sem que seus amiginhos vejam")
fala.runAndWait()

palavra = input("Digite a palavra: ")

fala.say("Agora espere seus amiginhos adivinhar a palavra, ou errar kkkkkk")
fala.runAndWait()

print("Fica a dica a palavra tem {} letras".format(len(palavra)))

erros = 0

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
print("Palavra com 4 letras")
print("todo mundo já falou ou ouviu falar")
print("É um dos maiores temas de filmes e séries")
i = input("Digite uma letra ou a palavra que acha: ")
c = 0

while c < 5:
    if i == "amor" or  i == "Amor":
        print("Você acertou!")

    elif i == "a":
        print("a***")
        c = c + 1
    elif i == "m":
        print("*m***")
        c = c + 1
    elif i == "o":
        print("**o*")
        c = c + 1
    elif i == "r":
        print("***r")
        c = c + 1
    else:
        print("Sua cabeça já está na corda")
        i = input("Digite uma letra ou a palavra que acha: ")
        c = c + 1
'''