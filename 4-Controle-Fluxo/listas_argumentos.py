def parrot(voltage, state="a stiff", action='voom'):
    print("-- this parrot wouldn't", action, end=' ')
    print("if you put", voltage,  "volts through it", end=" ")
    print("e's", state, "1")
    
d = {
    "voltage": "four million",
    "state": "bleedin",
    "action": "voom"
}

parrot(**d)
