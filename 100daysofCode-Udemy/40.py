try:
    f = open('testfile', 'r')
    f.write("Write a test line")
except TypeError:
    print('There was type error')
except OSError:
    print('There was os error')
finally:
    print('I always run')
