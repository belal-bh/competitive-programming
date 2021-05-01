import math
import random
a, b = map(int, input().split())

def solve(a, b):
    year = math.floor((math.log10(b/a) / math.log10(3/2)) + 1)
    return year


def slow(a, b):
    year = 0
    while not (a > b):
        year += 1
        a *= 3
        b *= 2
        # print(a, b, year)
    return year

# print(slow(a, b))
print(solve(a, b))

##########################
# RUN TEST
##########################
'''
q = 1000
count = 0
for i in range(q):
    b = random.randint(1, 10)
    a = random.randint(1, b)
    right = slow(a, b)
    test = solve(a, b)
    if right != test:
        print(f"WRONG! => ({a}, {b}): r={right}, t={test}")
        count += 1
    else:
        print(f"OK ({a}, {b}): r={right}, t={test}")
print(f"TEST: wrong= {count} / {q}")
'''