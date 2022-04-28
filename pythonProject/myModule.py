import math

mypi = math.pi

def factorial(n):
    y = 1
    for x in range(1, n + 1):
        y = y * x
    return y


def rFactorial(n):
    y = 1
    if n == 1:
        return 1
    else:
        return n * rFactorial(n - 1)
