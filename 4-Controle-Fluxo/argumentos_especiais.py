# podemos tanto chamar por posição quanto por nome
def standard_arg(arg):
    print(arg)
    
# podes chamar somete por posição se chamarmos por nome gera uma exceção
def pos_only_arg(arg, /):
    print(arg)

# podemos chmar somente pelo nome se chamarmos por posição gera uma exçeção
def kwd_only_arg(*, arg):
    print(arg)

# combimanos os estilos
def combined_exmaple(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)


standard_arg('ola')
standard_arg(arg="oi")

pos_only_arg('ola')

kwd_only_arg(arg="ola")

combined_exmaple("ola", standard='ola', kwd_only='oi')
combined_exmaple("ola", 'ola', kwd_only='oi')