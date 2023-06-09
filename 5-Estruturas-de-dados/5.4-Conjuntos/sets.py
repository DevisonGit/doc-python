"""
Set - são uma coleção desordenada de elementos sem repetição
Usados normalmente para remover objetos repetidos 
Suportam operações de união, interseção, diferença e diferença simetrica
"""
# para criar um set podemos usar set() ou {} com elementos, chaves vazias criam um dict
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(f"conjunto: {basket}")

# verificando se orange esta no conjunto
print(f"contem 'orange' no conjunto: {'orange' in basket}")

# verificando se crabgrass esta no conjunto
print(f"contem 'crabgrass' no conjunto: {'crabgrass' in basket}")

# criando conjuntos para realizar operações
a = set('abracadabra')
print(f"set a = {a}")
b = set('alacazam')
print(f"set b = {b}")

# união 
print(f"União a | b = {a | b}")

# interseção
print(f"Interseção a & b = {a & b}")

# diferença
print(f"Diferença a - b = {a - b}")
print(f"Diferença b - a = {b - a}")

# diferença simetrica
print(f"Diferença simetrica a ^ b = {a ^ b}")

# comprehension de conjuntos são suportadas
a = {x for x in 'abracadabra'}
print(f"set comprehension de 'abracadabra' {a}")
a = {x for x in 'abracadabra' if x not in 'abc'}
print(f"set comprehension de 'abracadabra' filtrando 'abc' {a}")