teste_string = "Salve o Corinthians o campeao dos campeoes"

separa = teste_string.split()
print(separa) #esse comando fragmenta a frase
busca = teste_string.find("dos")
print(busca)
print(teste_string[busca:]) #mostra apenas a frase após campo "dos"
teste_string = teste_string.replace("Corinthians","Palmeiras") #substituí string específica
print(teste_string)