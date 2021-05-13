s, t = input(), input()


def solve(s, t):
    x1, y1 = ord(s[0]) - 96, int(s[1])
    x2, y2 = ord(t[0]) - 96, int(t[1])
    # print(f"{s}:{x1},{y1} \n{t}:{x2},{y2}")

    x = x2-x1
    y = y2-y1
    d = []
    min_move = min(abs(x), abs(y))
    max_move = max(abs(x), abs(y))
    if max_move == 0:
        return 0, None

    if x > 0:
        d.append('R')
    elif x < 0:
        d.append('L')
    else:
        d.append('')

    if y > 0:
        d.append('U')
    elif y < 0:
        d.append('D')
    else:
        d.append('')

    # print(d)

    if abs(x) == abs(y):
        path = f"{''.join(d)}\n"*max_move
    elif abs(x) > abs(y):
        path = f"{d[0]}\n"*(max_move - min_move) + f"{''.join(d)}\n"*min_move
    else:
        path = f"{d[1]}\n"*(max_move - min_move) + f"{''.join(d)}\n"*min_move

    return max_move, path


moves, path = solve(s, t)
print(moves)
if path:
    print(path, end='')
