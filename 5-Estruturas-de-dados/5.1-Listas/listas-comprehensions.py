import time

# compreensões de lista é uma maneira concisa de criar listas


# lista de quadrados sem comprehensions
squares = []
inicio = time.time()
for x in range(1000000):
    squares.append(x ** 2)
fim = time.time()
print(f"sem list comprehensions tempo {fim - inicio}")

# lista de quadrados com comprehensions
inicio = time.time()
squares = [x**2 for x in range(1000000)]
fim = time.time()
print(f"com list comprehensions tempo {fim - inicio}")

# lista de quadrados com comprehensions outro exemplo
inicio = time.time()
squares = list(map(lambda x: x**2, range(1000000)))
fim = time.time()
print(f"com list comprehensions + map + lambda tempo {fim - inicio}")

# outro exemplo usando if
combs = [(x, y) for x in [1, 2, 3] for y in [3, 2, 4] if x != y]
print(combs)

# criando outra lista com o dobro
vec = [-4, -2, 0, 2, 4]
print(f" lista vec \n{vec}")
double_vec = [x**2 for x in vec]
print(f" lista vec com valores dobrados \n{double_vec}")

# filtrando numeros negativos
vec_positivos = [x for x in vec if x >= 0]
print(f" lista vec só valores positivos \n{vec_positivos}")

# aplicando a função abs para a lista vec
vec_abs = [abs(x) for x in vec]
print(f" lista vec função abs \n{vec_abs}")

# aplicando um metodo nos elementos da lista
fruits = [' banana ', ' loganberry ', ' pasion fruit']
fruits_metodo = [fruit.strip() for fruit in fruits]
print(f" lista fruit sem strip \n{fruits}")
print(f" lista fruit com strip \n{fruits_metodo}")

# criando uma lista com o numero e seu quadrado
lista = [(x, x**2) for x in range(10)]
print(f" lista com numero e quadrado \n{lista}")

# nivelando uma lista
vec = [[1,2,3], [4,5,6], [7,8,9]]
vec_nivelado = [y for x in vec for y in x]
print(f" lista nivelada \n{vec_nivelado}")

# comprehensions podem conter expressões complexas e funçoes aninhadas
from math import pi
pis = [str(round(pi, i)) for i in range(1, 6)]
print(f" lista complexas e com funções aninhadas \n{pis}")
