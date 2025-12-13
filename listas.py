my_list = [1, 2, 3, 4, 5]
my_list_2 = ["avocado", "banana", "cherry", "strawberry", "kiwi"]
my_list_3 = [] # lista vazia
print(my_list_2)
print(my_list_2[2])


for item in my_list_2:
    print(item)

tamanho = len(my_list_2)
print(tamanho)

my_list_2.append("orange") # insere um novo item na lista
print(my_list_2)

if "banana" in my_list_2:
    print("Banana está na lista")
if 10 not in my_list:
    print("10 não está na lista")

del my_list[0:2]  # remove do primeiro ao terceiro item da lista
print(my_list)

my_list_3.append("mango") # adiciona um item à lista vazia
print(my_list_3)