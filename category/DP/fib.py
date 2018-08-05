# calculate n'th fibonacci number using dictionary and DP

from bhpack import timing
memo = {'0': 0, '1': 1}


def fib(n):
    if str(n) in memo:
        return memo[str(n)]
    if n < 1:
        return 0
    f = fib(n - 1) + fib(n - 2)
    memo[str(n)] = f
    return f


n = 20
n = int(input("Enter a number:"))
print("{}'th fib= {} \n".format(n, fib(n)))
# for i in range(0, n):
#     print("{}'th fib= {} \n".format(i, fib(i)))
