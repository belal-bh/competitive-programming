# TLE
n, m = map(int, input().split())
a = list(map(int, input().split()))
f = [1, 1]
for i in range(2, n):
    f.append(f[i-1]+f[i-2])

def sum_of_a_fib(l, r):
    for i in range(l-1, r):
        a[i] += f[i-l+1]

def mod_of_sum_of_range(l, r):
    lr_sum = 0
    for i in range(l-1, r):
        lr_sum += a[i]
    return lr_sum % 1000000009

for _ in range(m):
    qf, l, r = map(int, input().split())
    if qf == 1:
        sum_of_a_fib(l, r)
        # print(a)
    elif qf == 2:
        print(mod_of_sum_of_range(l, r))
