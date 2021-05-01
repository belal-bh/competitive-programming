###### TLE ########
# import re

class WordFilter:

    def __init__(self, words):
        self.words = words[::-1]
        self.ws_len = len(words)
        self.w_lens = [len(w) for w in words]
        self.w_max_len = max(self.w_lens)
        self.w_min_len = min(self.w_lens)

    def f(self, prefix, suffix):
        pre_len = len(prefix)
        suf_len = len(suffix)
        is_identical = False
        if pre_len > self.w_min_len or suf_len > self.w_min_len:
            return -1
        if prefix == suffix:
            is_identical = True

        for word, index, i in zip(self.words, range(self.ws_len-1, -1, -1), range(self.ws_len)):
            if pre_len > self.w_lens[i] or suf_len > self.w_lens[i]:
                continue
            else:
                if is_identical and self.w_lens[i] == pre_len:
                    if word == prefix:
                        return index
                    continue
                if prefix == word[0:pre_len] and suffix == word[self.w_lens[i]-suf_len:]:
                    return index

            # pattern_pre = f'^{prefix}.*'
            # pattern_suf = f'.*{suffix}$'
            # if re.search(pattern_pre, word) and re.search(pattern_suf, word):
            #     return index
        return -1

# words = ['apple', 'aphdjfheee']
# prefix, suffix = 'ap', 'eee'
# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)

# print(param_1)


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
