import random
die = random.SystemRandom()  # A single dice

def single_test(n,a):
    exp = n - 1
    while not exp & 1: #sve dok nismo dosli do neparnog broja
        exp >>= 1
    if pow(a,exp,n) == 1:
        return True
    while exp < n - 1:
        if pow(a, exp, n) == n - 1:
            return True
        exp <<= 1
    return False

def miller_rabin(n, k= 5):
    yes = no = 0
    for i in range(k):
        a = die.randrange(2, n - 1)
        if not single_test(n,a):
            no = no + 1
        else:
            yes = yes + 1

    res = yes > no
    return res

print(miller_rabin(35435363557993133))
#print(single_test(29,10))