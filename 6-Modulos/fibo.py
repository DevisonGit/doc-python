"""
Um modulo é um arquivo contendo definições e instruções Python
Importar um modulo -> import modulo_name
Importar especificando -> from modulo_name import modulo
Importar tudo do modulo -> from modulo_name import *
o metodo dir() exibe uma lista de todos os nomes definidos por um modulo
Pacotes são uma maneira de estruturar modulos
"""

# Fibonacci modulos
def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()


def fib2(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

if __name__ == '__main__':
    import sys
    fib(int(sys.argv[1]))