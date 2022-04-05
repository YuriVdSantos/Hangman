import pyttsx3

fala = pyttsx3.init()

fala.say("Olá humano, bem-vido ao jogo da Forca! Por favor, digite a palavra que você deseja adivinhar"
", mas sem que seus amiguinhos vejam")
fala.runAndWait()

palavra = input("Digite a palavra: ")

lista_palavra = list(palavra)

letras_acertadas = []
erros = 0

fala.say("Agora espere seus amiguinhos adivinhar a palavra, ou errar kkkkkk")
fala.runAndWait()

print("Fica a dica a palavra tem {} letras".format(len(palavra)))
fala.say("Lembrando que você só pode errar {} vezes".format(len(palavra)))
fala.runAndWait()

for i in range(0, len(lista_palavra)):
    letras_acertadas.append("*")

acertou = False

while acertou == False:
    letra = str(input("Digite uma letra: "))

    if erros == len(palavra):
        print("Você perdeu, a palavra era {}".format(palavra))
        fala.say("Você perdeu, a palavra era {}".format(palavra))
        fala.runAndWait()
        break

    for i in range(0, len(palavra)):
        if letra == palavra:
            fala.say("Aeeeeeeeeeeeeeeeeeeeee")
            fala.runAndWait()
            print("Você acertou, a palavra é {}".format(letra))
            exit()
        elif letra == lista_palavra[i]:
            letras_acertadas[i] = letra
    erros += 1
        

    palavra_acertada = "".join(letras_acertadas)
    print(palavra_acertada)

    acertou = True
    for x in range(0, len(letras_acertadas)):
        if letras_acertadas[x] == "*":
            acertou = False
            break

fala.say("Aeeeeeeeeeeeeeeeeeeeee")
fala.runAndWait()
print("Você acertou, a palavra é {}".format(palavra_acertada))
