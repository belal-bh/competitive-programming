import itertools as it
import re


class Solution:
    def __init__(self):
        pattern = "(?:^0{2,9}.*$)|(?:^0{1,9}[0-9]+.*$)|(?:^.*[.]+[0-9]*0{1,9}$)"
        self.pattern = re.compile(pattern)

    def ambiguousCoordinates(self, s):
        s = s[1:-1]
        c = [(s[:i], s[i:]) for i in range(1, len(s))]
        R = []
        for x, y in c:
            for i in range(0, len(x)):
                for j in range(0, len(y)):
                    cor = []
                    if i == 0 and j == 0:
                        cor.append((x, y))
                    elif i == 0:
                        cor.append((x, y[:j]+'.'+y[j:]))
                    elif j == 0:
                        cor.append((x[:i]+'.'+x[i:], y))
                    else:
                        cor.append((x[:i]+'.'+x[i:], y[:j]+'.'+y[j:]))

                    clean_cor = self.clean(cor, stringify=True)
                    if clean_cor:
                        R.append(clean_cor[0])
        return R

    def clean(self, cross, stringify=False):
        clean_list = []
        updated_list = []
        for i, (x, y) in enumerate(cross):
            if self.pattern.match(x) or self.pattern.match(y):
                continue
            elif stringify:
                clean_list.append(f"({x}, {y})")
            else:
                updated_list.append((x, y))

        if stringify:
            return clean_list
        return updated_list


# s = '(0123)'
# obj = Solution()
# res = obj.ambiguousCoordinates(s)
# print(res)
