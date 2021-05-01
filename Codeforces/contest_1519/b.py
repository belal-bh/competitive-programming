t = int(input())

def solve(n, m, k):
    if (n*m - 1) == k:
        return 'YES'
    return 'NO'

while t > 0:
    t -= 1
    n, m, k = map(int, input().split())
    print(solve(n, m, k))
