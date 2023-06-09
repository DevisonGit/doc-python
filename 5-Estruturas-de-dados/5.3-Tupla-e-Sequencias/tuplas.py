# Uma tupla é uma sequencia de valores separados por virgula
t = 12345, 54321, 'hello!'
print(f"uma tupla: {t}")

# podemos acessar um elemento pelo indice
print(f"uma tupla: {t[0]}")

# podemos unir tuplas
u = t, (1, 2, 3, 4, 5)
print(f"unindo duas tuplas: {u}")

# tupla são imultaveis, portando t[0] = 8888 gera um erro
# mas as tuplas podem conter elementos mutaveis com uma lista
v = ([1, 2, 3], [3, 2, 1])
print(f"tupla com elementos mutaveis: {v}")

# empacotamento de uma tupla
t = 12345, 54321, 'hello!'

# desempacotando uma tupla, requer que tenha a mesma quantidade de
# variaveis do lado esquerdo quanto existem de elemntos na tupla
x, y, z = t
