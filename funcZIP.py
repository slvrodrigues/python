#concatena listas com zip
lista1 = [1, 2, 3]
lista2 = ['a', 'b', 'c']
for numero, letra in zip(lista1, lista2):
    print(f"Número: {numero}, Letra: {letra}")