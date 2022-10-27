#From any value n, such that n > 1, print on the screen a square made of asterisks with sides of size n

def draw_square(n):
    for row in range(n):
        print(n * '*')


draw_square(8)