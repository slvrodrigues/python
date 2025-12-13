with open("arquivo.txt", "w", encoding="utf-8") as w:
    w.write("Primeira linha em UTF-8\n")
with open("arquivo.txt", "a") as w:
    w.write("\nAdicionando uma nova linha ao arquivo") # append - acrescenta ao final do arquivo