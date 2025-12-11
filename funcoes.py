#sao definidas pela palavra reservada def sendo seu bloco executado somente se for chamado

def soma(x, y):
    print(x + y)
soma(2,3)

def soma(x, y):
    return x+y #forma usando return
#s= soma(2,3)
#print(s)

def multiplicacao(x, y):
    return x*y

s = soma(2, 3)
m = multiplicacao(3, 4)

print(soma(s,m)) 
