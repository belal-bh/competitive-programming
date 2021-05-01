a, b, n = map(int, input().split())

def solve(a, b, n):
    for i in range(n):
        a *= 10
        dmin = a//b
        dmax = (a+9)//b
        if a%b == 0:
            a = int(str(a)+ '0'*(n-i-1))
            break
        elif dmin < dmax:
            d = (dmin+1)*b - a
            if d > 9:
                a = -1
                break
            else:
                a += d
        else:
            a = -1
            break
    return a

print(solve(a, b, n))