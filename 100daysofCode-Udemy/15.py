def makes_twenty(n1,n2):
    if n1 + n2 == 20:
        return True
    elif n1 == 20:
        return True
    elif n2 == 20:
        return True
    else:
        return False

print(makes_twenty(20,3))
print(makes_twenty(2,3))