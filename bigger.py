#function that takes two numbers and returns the largest of them.

def bigger(number, other):
    if other > number:
        return other
    return number

print(bigger(4,3))