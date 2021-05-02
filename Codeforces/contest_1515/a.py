t = int(input())

while t > 0:
    t -= 1
    n, x = map(int, input().split())
    w = list(map(int, input().split()))

    w_len = len(w)
    wt = 0
    res = True
    for i in range(w_len):
        wt += w[i]
        if wt == x:
            if i == (w_len - 1):
                res = False
                break
            else:
                w[i], w[i+1] = w[i+1], w[i]
                break
        elif wt > x:
            break
    if res:
        print('YES')
        print(*w, sep=' ')
    else:
        print('NO')
