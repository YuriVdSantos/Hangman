import random

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

        