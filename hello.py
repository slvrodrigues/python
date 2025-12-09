
# Meu primeiro programa, e isso é um comentário
print ("Hello World") 
"""
comentarios de 
multiplas 
linhas

"""
print ("Olá Mundo!") # Python 3 já oferece suporte nativo a caracteres com acentuação, eliminando o uso do coding utf8
# operações 
print(2+2)
print(2*2)
print(2**3) #exponenciação
print(10%3) #operação com mod, mostrando o resto

for i in range(5): #laco de repetição com for
	print("mensagem")
#lacos com while
contador = 0
while contador < 5:
    print("Sua mensagem aqui")
    contador += 1

contador = 0
while contador < 10:
	print(f"mensagem {contador}")
	contador += 1
	
var1 = 1 #variavel inteira
var2 = 1.1 #variavel float
var3 = "Eu sou uma string" #variavel string
var4 = True #variavel booleana
print(var1)
print(var2)
print(var3)
print(var4)

x = 2
y = 3
soma = x + y
print(x == y) #operador relacional

k = 2
j = 2
v = 3
print(k == j or k == v and v == j)
