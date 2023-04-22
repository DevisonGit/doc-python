def ask_ok(prompt, retries=4, reminder='Please try again!'):
    """ função com valores padrões para alguns argumentos """
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

ask_ok("ola")
        