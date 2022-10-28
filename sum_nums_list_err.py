numeros = input("Insira valores numericos aqui, separados por espaço: ")

array_de_numeros = numeros.split(" ")

soma = 0

for numero in array_de_numeros:
    if not numero.isdigit():
        print(f"Erro ao tentar somar, {numero} não é um número válido")
    else:
        soma += int(numero)

print(f"A soma dos valores é: {soma}")
