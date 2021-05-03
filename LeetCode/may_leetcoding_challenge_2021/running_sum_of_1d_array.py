class Solution:
    def runningSum(self, nums):
        for i in range(1, len(nums)):
            nums[i] = nums[i-1] + nums[i]
        return nums


# nums = [x for x in range(10)]
# obj = Solution()
# res = obj.runningSum(nums)
# print(res)
