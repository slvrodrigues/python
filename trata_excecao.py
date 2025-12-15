a = 2
b = 0

try:
    resultado = a / b
    print("O resultado da divisão é:", resultado)
except ZeroDivisionError: # Captura a exceção de divisão por zero
    print("Erro: Divisão por zero não é permitida.")

print (a/a)