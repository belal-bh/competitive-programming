import itertools


class Solution:
    def maxScore(self, cp, k):
        n = len(cp)
        if n == k:
            return sum(cp)
        cu_cp = list(itertools.accumulate(cp))
        max_score = 0
        for i in range(k+1):
            if i == 0:
                b = 0
                f = cu_cp[k-i-1]
            elif i == k:
                f = 0
                b = cu_cp[-1] - cu_cp[-i] + cp[-i]
            else:
                f = cu_cp[k-i-1]
                b = cu_cp[-1] - cu_cp[-i] + cp[-i]
            max_score = max(max_score, f+b)
        return max_score


# cp = [1, 79, 80, 1, 1, 1, 200, 1]
# k = 3
# obj = Solution()
# res = obj.maxScore(cp, k)
# print(res)
