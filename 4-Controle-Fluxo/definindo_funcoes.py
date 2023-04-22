def fib(n: int):
    """imprime uma serie Fibonacci até n """
    a, b = 0, 1
    while a < n:
        print(a, end= ' ')
        a, b = b, a + b
    print()

fib(2000)

def fib2(n):
    """ retorna uma serie fibonacci"""
    a, b = 0, 1
    result = []
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result

fibo = fib2(2000)
print(fibo)
        