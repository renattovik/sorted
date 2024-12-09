import random


def embaralhar_e_ordenar_seis_dezenas():
    # Solicita ao usuário que insira os números separados por espaços
    numeros = input("Digite os números separados por espaços: ").split()

    # Converte a lista de strings em uma lista de inteiros
    numeros = [int(numero.strip()) for numero in numeros]

    # Verifica se há pelo menos seis números
    if len(numeros) < 6:
        print("Por favor, insira pelo menos seis números.")
        return

    # Embaralha a lista de números
    random.shuffle(numeros)

    # Seleciona as primeiras seis dezenas embaralhadas
    seis_dezenas = numeros[:6]

    # Ordena as seis dezenas em ordem crescente
    seis_dezenas.sort()

    # Imprime os números em ordem crescente
    print("Seis dezenas embaralhadas e ordenadas:", sorted(seis_dezenas))


# Executa a função
embaralhar_e_ordenar_seis_dezenas()




