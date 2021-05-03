### Accepted ###
from functools import cmp_to_key
n = int(input())


d = {}
for r in range(1, n+1):
    k, v = input().split()
    v = int(v)
    if d.get(k, None):
        d[k].append([d[k][-1][0]+v, r])
    else:
        d[k] = [[v, r]]


players = [[k, v[-1][0], v] for k, v in d.items()]
players.sort(key=lambda x: x[1], reverse=True)

max_score = players[0][1]
first_acv = 10009
winner = ''
i = 0
while i < len(players):
    if players[i][1] == max_score:
        for st in players[i][2]:
            if st[0] >= max_score:
                if first_acv > st[1]:
                    first_acv = st[1]
                    winner = players[i][0]
                    break
    else:
        break
    i += 1

print(winner)
