# uso basico do formar()
print('we are the {} who say "{}!"'.format('knights', 'ni'))

# o numero nas chaves podem referenciar a posição do objeto passado
print('{0} and {1}'.format('spam', 'eggs'))
print('{1} and {0}'.format('spam', 'eggs'))

# podemos usar argumentos nomeados
print('This {food} is {adjective}'.format(
    food='spam', adjective='absolutely horrible'))

# argumento posicionais e nomeados podem ser combinados
print('the story of {0}, {1} and {other}'.format(
    'Bill', 'Manfred', other='Georg'))

# referencia aos valores 
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
      'Dcab: {0[Dcab]:d}'.format(table))

# usando a notação **
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; '
      'Dcab: {Dcab:d}'.format(**table))

# coluna alinhadas
for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
