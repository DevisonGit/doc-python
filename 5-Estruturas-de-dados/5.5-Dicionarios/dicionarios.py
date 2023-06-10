"""
O tipo dict é uma estrutura de dados que utiliza chave:valor
a chave deve ser de um tipo imutavel e unica, um dict vazio é {}
"""

# Criando um dict
tel = {'jack': 4098, 'sape': 4139}
print(f"dict {tel}")

# adicionado um elemento no dicionario
tel['guido'] = 4127
print(f"dict {tel}")

# exibindo o valor de uma chave
print(f"valor da chave jack: {tel['jack']}")

# deletando chave:valor de um dicionario
del tel['sape']
print(f"excluindo 'sape': {tel}")

# listando as chaves de um dict
print(f"lista de chaves: {list(tel)}")

# listando de forma ordenada um dict
print(f"lista ordenada de chaves: {sorted(tel)}")

# verificando de exite uma determinada chave
print(f"existe a chave 'guido' : {'guido' in tel}")
print(f"não existe a chave 'jack' : {'jack' not in tel}")

# construtor dict produz dicionarios diretos de sequencias de chave:valor
a = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print(f"usando contrutor lista e tupla : {a}")

# comprehension
num = {x: x**2 for x in [2, 4, 6]}
print(f"usando comprehension : {num}")

# chave string simples no contrutor do dict
a = dict(sape=4139, guido=4127, jack=4098)
print(f"usando contrutor string simples : {a}")