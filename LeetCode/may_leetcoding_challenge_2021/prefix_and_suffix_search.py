###### Accepted  ########

class WordFilter:

    def __init__(self, words):
        self.d = {}
        for i, w in enumerate(words):
            w_len = len(w)
            for p in range(1, min(10, w_len)+1):
                for s in range(1, min(10, w_len)+1):
                    self.d[w[:p], w[-s:]] = i

    def f(self, prefix, suffix):
        return self.d[prefix, suffix] if (prefix, suffix) in self.d else -1


""" TEST
data = [[["cabaabaaaa", "ccbcababac", "bacaabccba", "bcbbcbacaa", "abcaccbcaa", "accabaccaa", "cabcbbbcca", "ababccabcb", "caccbbcbab", "bccbacbcba"]], ["bccbacbcba", "a"], [
    "ab", "abcaccbcaa"], ["a", "aa"], ["cabaaba", "abaaaa"], ["cacc", "accbbcbab"], ["ccbcab", "bac"], ["bac", "cba"], ["ac", "accabaccaa"], ["bcbb", "aa"], ["ccbca", "cbcababac"]]
output = []
for i in range(1, len(data)):
    obj = WordFilter(data[0][0])
    index = obj.f(data[i][0], data[i][1])
    output.append(index)
    # print(index)

print(output)
"""
