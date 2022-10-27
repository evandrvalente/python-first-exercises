#Calculate the arithmetic mean of the values contained in a list.

def mean(numbers):
    total = 0
    for number in numbers:
        total += number
    return total / len(numbers)

lista_de_numeros = [6, 5, 7, 9]
print(mean(lista_de_numeros))