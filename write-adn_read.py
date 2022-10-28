# escrita
file = open("arquivo.txt", mode="w")
file.write("Viva la vida")
file.close()

# leitura
file = open("arquivo.txt", mode="r")
content = file.read()
print(content)
file.close()
