def cool():
    def supercool():
        return 'I am very cool'

    return supercool


some_func = cool()

print(some_func())
