import random


def embaralhar_lista():
    # Solicita ao usuário que insira os números separados por vírgulas
    numeros = input("Digite os números separados por vírgulas: ").split(",")

    # Converte a lista de strings em uma lista de inteiros
    numeros = [int(numero.strip()) for numero in numeros]

    # Embaralha a lista de números
    random.shuffle(numeros)

    print("Números embaralhados:", numeros)


# Executa a função
embaralhar_lista()
