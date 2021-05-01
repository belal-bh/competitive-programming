###### TLE ########
# import re

class WordFilter:

    def __init__(self, words):
        self.words = words

    def f(self, prefix, suffix):
        for word, index in zip(self.words[::-1], range(len(self.words)-1, -1, -1)):
            # print(prefix, word, suffix)
            pre_len = len(prefix)
            suf_len = len(suffix)
            w_len = len(word)
            if pre_len > w_len or suf_len > w_len:
                continue
            else:
                if prefix == word[0:pre_len] and suffix == word[w_len-suf_len:]:
                    return index


            # if prefix == suffix and len(word) == len(prefix):
            #     if word == prefix:
            #         return index
            #     else:
            #         continue
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

# data = [[["cabaabaaaa","ccbcababac","bacaabccba","bcbbcbacaa","abcaccbcaa","accabaccaa","cabcbbbcca","ababccabcb","caccbbcbab","bccbacbcba"]],["bccbacbcba","a"],["ab","abcaccbcaa"],["a","aa"],["cabaaba","abaaaa"],["cacc","accbbcbab"],["ccbcab","bac"],["bac","cba"],["ac","accabaccaa"],["bcbb","aa"],["ccbca","cbcababac"]]
# output = []
# for i in range(1, len(data)):
#     obj = WordFilter(data[0][0])
#     index = obj.f(data[i][0],data[i][1])
#     output.append(index)
#     print(index)

# print(output)