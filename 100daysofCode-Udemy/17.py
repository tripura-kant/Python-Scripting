#

def master_yoda(text):
    wordlist = text.split()
    reversed_word = wordlist[::-1]
    return ' '.join(reversed_word)

print(master_yoda('T am I'))
