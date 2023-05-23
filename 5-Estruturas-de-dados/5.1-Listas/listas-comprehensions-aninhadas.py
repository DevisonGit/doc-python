# a expressão inicial de um comprehensions pode ser uma expressão arbitratria
# ou outra list comprehensions

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
print([[row[i] for row in matrix] for i in range(4)])

# porem na pratica devemos usar funções embutidas o zip faz o mesmo
print(list(zip(*matrix)))