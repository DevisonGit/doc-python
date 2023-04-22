def parrot(voltage, state='a stiff', action='voom', type='norwegian blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print('if you put', voltage, 'volts through it')
    print('-- lovely plumage type', type)
    print("-- it's", state, '!')
    
    
def cheeseshop(kind, *args, **kwargs):
    print("-- Do you have any", kind)
    print("-- i'm sorry, we're all out of", kind)
    # o *args é uma tupla
    for arg in args:
        print(arg)
    # o **kwargs é um dicionario
    for arg in kwargs:
        print(arg, ":", kwargs[arg])
        
    
parrot(1000)
print()
cheeseshop("limburger", 
           "it's very runny, sir",
           "it's really very very runny, sir",
           shopkeeper="Michael palin",
           client="jonh clesse",
           sketch="chesse shop sketch")