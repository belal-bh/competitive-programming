t = int(input())


def solve(tasks):
    d = {}
    l = len(tasks)
    i = 0
    while i < l:
        if d.get(tasks[i], None):
            return 'NO'
        else:
            d[tasks[i]] = True
            ct = tasks[i]
            i += 1
            while i < l:
                if tasks[i] != ct:
                    i -= 1
                    break
                i += 1
        i += 1
    return 'YES'


while t > 0:
    t -= 1
    n = int(input())
    tasks = input()

    print(solve(tasks))
