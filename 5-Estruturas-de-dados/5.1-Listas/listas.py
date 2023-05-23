# criando uma lista
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

# numero de vezes que o argumento aparece na lista
print(f"qtd de 'apple' na lista: {fruits.count('apple')}")
print(f"qtd de 'tangerine' na lista {fruits.count('tangerine')}")

# primeira ocorrencia do argumento na lista
print(f"indice da primeira ocorrencia de 'banana' na lista: {fruits.index('banana')}")
print(f"indice da primeira ocorrencia de 'banana' começando no indice 4 da lista: {fruits.index('banana', 4)}")

# inverte a ordem da lista
print(f"antes do reverse {fruits}")
fruits.reverse()
print(f"depois do reverse {fruits}")

# inseri o argumento no final da lista
fruits.append('grape')
print(f"inserindo 'grape' na lista {fruits}")

# ordena a lista
print(f"antes do sort {fruits}")
fruits.sort()
print(f"depois do sort {fruits}")

# excluindo com pop
print(f"antes do pop {fruits}")
print(f"excluindo com pop sem indice: {fruits.pop()}")
print(f"excluindo com pop com indice: {fruits.pop(0)}")
print(f"depois do pop {fruits}")

# extendendo a lista com o argumento passado
fruits.extend(['tomato', 'mango'])
print(f"usando o extends com outra lista ['tomato', 'mango']: {fruits}")

# cria uma copia rasa da lista.
fruits_two = fruits.copy()
print(f"lista original {fruits}")
print(f"lista copia {fruits_two}")
fruits_two.append('pineapple')
print(f"apos inserir 'pineaple' na lista copia, lista original: {fruits}")
print(f"lista copia: {fruits_two}")

# limpando toda a lista
fruits.clear()
print(f"limpando toda a lista com clear: {fruits}")