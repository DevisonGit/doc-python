# podemos formatar a saida usando f ou F antes de abrir as apas
year = 2023
event = "Nada"
print(f'Ano {year} Evento {event}')
print(F'Ano {year} Evento {event}')

# usando format()
yes_votes = 42_572_654
no_votes = 43_132_495
percentage = yes_votes / (yes_votes + no_votes)
print('{:-9} Yes votes {:2.2%}'.format(yes_votes, percentage))

# o metodo str() retorna representações de valores legiveis para pessoas
s = 'hello, world\n'
print(f"str(s) -> {str(s)}")
print(f"str(1/7) -> {str(1/7)}")

# o metodo repr() retorna representações de valores legivel para o python
print(f"repr(s) -> {repr(s)}")
print(f"repr(1/7) -> {repr(1/7)}")
