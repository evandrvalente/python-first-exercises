# escrita
file = open("arquivo2.txt", mode="w")
LINES = ["Olá\n", "mundo\n", "belo\n", "do\n", "Python\n"]
file.writelines(LINES)
file.close()

# leitura
file = open("arquivo2.txt", mode="r")
for line in file:
    print(line)
file.close()
