import random
#random.seed()  # Inicializa o gerador de números aleatórios ou força um numero específico
numero = random.randint(1, 60)
print("Número sorteado:", numero)

lista = [6,9,45]
numero = random.choice(lista)
print("Número escolhido da lista:", numero)

#codigo de exemplo para loteria do tipo mega-sena
import random

numeros = random.sample(range(1, 61), 6)
print("Números sorteados:", numeros)

import random

numeros = sorted(random.sample(range(1, 61), 6)) # Ordena os números sorteados
print("Números sorteados:", numeros)

#código de exemplo para loteria do tipo lotofácil
numeros = sorted(random.sample(range(1, 26), 15)) # Ordena os números sorteados
print("Números sorteados:", numeros)


#código de exemplo para gerar vários jogos de loteria

import random

for i in range(5):
    jogo = sorted(random.sample(range(1, 61), 6))
    print(f"Jogo {i+1}: {jogo}")
