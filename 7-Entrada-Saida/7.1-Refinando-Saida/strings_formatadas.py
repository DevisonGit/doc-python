import math

# passando um inteiro apos : faz que o campo tenha um numero caracteres
print(f"O valor de PI é aproxiamdamente: {math.pi:.3f}")

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for nome, numero in table.items():
    print(f"{nome:10} ==> {numero:10d}")

# !a aplica a função ascii()
animals = 'eels'
print(f'My hovercraft is full of {animals!a}.')

# !s aplica a função str()
print(f'My hovercraft is full of {animals!s}.')

# !r aplica a função repr()
print(f'My hovercraft is full of {animals!r}.')

# o = pode ser usado para expandir a expressão
bugs = 'roaches'
count = 13
area = 'living room'
print(f"Debugging {bugs=} {count=} {area=}")
