# para iterar sobre dicionarios
knigths = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knigths.items():
    print(k, v)

# para iterar sobre sequencias podemos usar o enumerate
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

# para percorrer duas sequencias ao mesmo tempo podemos usar o zip
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print(f'what is your {q}? It is {a}.')

# percorrendo uma sequencia em ordem inversa
for i in reversed(range(1, 10, 2)):
    print(i)

# percorre de maneira ordenada, não altera a lista
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for b in sorted(basket):
    print(b)

# percorre de maneira ordenada excluindo duplicidade, não altera a lista
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for b in sorted(set(basket)):
    print(b)

# ao inves de alterar uma lista é mais seguro e simples criar outra
import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for x in raw_data:
    if not math.isnan(x):
        filtered_data.append(x)
print(filtered_data)