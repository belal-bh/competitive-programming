import math
t = int(input())


def is_square(x):
    return math.isclose(x, int(math.sqrt(x))**2)


while t > 0:
    t -= 1
    n = int(input())

    if is_square(n/2) or is_square(n/4):
        print('YES')
    else:
        print('NO')
