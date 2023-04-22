i = 5

def f(arg=i):
    print(arg)
    
i = 6
# imprime 5 pois o valor padrão é definido no momento da função
f()

# acumula os valores para as outra chamadas
def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))

# valor padrão não é compartilhado na outras chamadas
def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))


