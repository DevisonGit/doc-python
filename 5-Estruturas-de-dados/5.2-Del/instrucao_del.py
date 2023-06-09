a = [-1, 1, 66.25, 333, 333, 1234.5]
print(f"lista original: {a}")

# deleta o elemento de indece 0
del a[0]
print(f"lista depois de del a[0]: {a}")

# deleta um fatia da lista
del a[2:4]
print(f"lista depois de del a[2:4]: {a}")

# deleta todas a lista, porem mantem a variavel
del a[:]
print(f"lista depois de del a[:]: {a}")

# apaga totalmente a variavel
del a
