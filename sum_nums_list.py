numeros = input("Insira valores numericos aqui, separados por espaçoo: ")

array_de_numeros = numeros.split(" ")

soma = 0

for numero in array_de_numeros:
    soma += int(numero)

print(f"A somados valores é: {soma}")
