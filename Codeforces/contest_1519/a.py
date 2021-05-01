t = int(input())

def solve(r, b, d):
    if r > b:
        r, b = b, r
    if r*(d+1) < b:
        return 'NO'
    return 'YES'

while t>0:
    t -= 1
    r, b, d = map(int, input().split())

    print(solve(r, b, d))