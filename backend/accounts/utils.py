import random
import string

def account():
    accounts = ''.join(random.choices('0123456789', k=4))
    Alphabet =list(string.ascii_uppercase)
    A = random.choice(Alphabet)
    B = random.choice(Alphabet)
    C = random.choice(Alphabet)
    accountNum = f'{A}{B}{C}{accounts}'

    return accountNum



