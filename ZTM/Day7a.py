# Scope- what variable do I have access to ?

a = 1

def confusion():
    a = 5
    return a

print(a)
print(confusion())

