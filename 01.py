import math


def qp(x):
    s = int(math.sqrt(x))
    return s * s == x


def fibonacci(y):
    return qp(5 * y * y + 4) or qp(5 * y * y - 4)


a = int(input("Digite um numero: "))

if fibonacci(a):
    print(f"{a} é um numero da sequencia de fibonacci")
else:
    print(f"{a} não pertence a sequencia de fibonacci")
