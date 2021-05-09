import random

t = int(input())


def solve(n_str):
    d = len(n_str)
    n = int(n_str)
    first_digit = int(n_str[0])

    res = d*9 - (9-first_digit)
    for i in range(1, d):
        if n_str[i] != n_str[0]:
            if int(n_str[i]) < int(n_str[0]):
                res -= 1
            break
    return res


while t > 0:
    t -= 1
    n_str = input()
    print(solve(n_str))

#### TEST ####
'''

def slow(n_str):
    n = int(n_str)
    res = 0
    for i in range(1, n+1):
        s = str(i)
        ordinary = 1
        for j in range(1, len(s)):
            if s[j] != s[0]:
                ordinary = 0
                break
        res += ordinary
    return res


i = 0
while i < 1000:
    i += 1
    n_max = 100000
    n_str = str(random.randint(1, n_max))
    a = solve(n_str)
    b = slow(n_str)
    if a != b:
        print(f"WRONG {n_str} -> {a}, {b} => dif:{a-b}")
        break
    else:
        print(f"OK {n_str} -> {a}, {b} => dif:{a-b}")
'''
