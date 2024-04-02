import random


while True:
        intervalo=range(0,11)

        num=random.choice(intervalo)
        print(f"4 x {num} = ? ")

        intervalo2=range(0,11)
        num2=random.choice(intervalo2)

        print(f"7 x {num2} = ? ")

        numeros = [4, 8, 12, 16, 20, 24, 28, 32, 36, 40]
        numemros2 = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]

        resp=int(input('Enntre com a Sua Resposta. '))
        resp2=int(input('Entre com a Sua Resposta '))

        if resp in numeros:
            print(f'Você Digitou\033[1;32m {resp}\033[m Número correto.')
        else:
            print(f' Você Digitou\033[1;32m  {resp} \033[m Número incorreto..')

        if resp2 in numemros2:
             print(f'Você Digitou \033[1;32m{resp2}\033[m Números correto.')
        else:
             print(f'Você Digitou\033[1;32m {resp2}\033[m Número Incorreto.')

        continuar = input("Deseja continuar? (s/n): ")

        # aqui o user descide se quer continuar
        if continuar.lower() != 's':
            break




#     import random

# # Define o intervalo de números (de 1 a 10)
# intervalo = range(1, 11)

# # Escolhe um número aleatório dentro do intervalo
# numero_aleatorio = random.choice(intervalo)

# # Imprime o número aleatório escolhido
# print("O número aleatório é:", numero_aleatorio)


# Lista de números
# numeros = [10, 5, 8, 12, 3, 15]

# # Número para comparar
# numero = 8

# # Verificando se o número está na lista
# if numero in numeros:
#     print(f"O número {numero} está na lista.")
# else:
#     print(f"O número {numero} não está na lista.")