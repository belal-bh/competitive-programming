class Solution:
    def jump(self, nums):
        n_len = len(nums)
        curr = -1
        nxt = 0
        res = 0
        i = 0
        while nxt < n_len - 1:
            if i > curr:
                res += 1
                curr = nxt
            nxt = max(nxt, nums[i]+i)
            i += 1
        return res


# nums = [2, 3, 1, 1, 4]
# obj = Solution()
# res = obj.jump(nums)
# print(res)
