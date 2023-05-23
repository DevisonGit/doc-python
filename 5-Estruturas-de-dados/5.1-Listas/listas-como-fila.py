# usando lista como fila (primeiro a entrar primeiro a sair) FIFO
lista = [1, 2, 3, 4, 5]
print(lista)
lista.append(6)
print(lista)
lista.append(7)
print(lista)
print(f"removendo o primeiro a entrar na lista {lista.pop(0)}")
print(lista)

# é recomendado usar a classe collections.deque pois ela foi projetada 
# para permitir appends e pops com eficiencia em ambas as extremidades da lista

from collections import deque

queue = deque([1, 2, 3])
print(queue)
queue.append(4)
queue.append(5)
queue.popleft()
print(queue)