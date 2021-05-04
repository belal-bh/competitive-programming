### Accepted ###
class Solution:
    def checkPossibility(self, nums):
        n = len(nums)
        ni = n-1
        for i in range(n-1):
            if nums[i] > nums[i+1]:
                if i+2 <= ni:
                    if nums[i+1] <= nums[i+2]:
                        if nums[i] <= nums[i+2]:
                            nums[i+1] = nums[i]
                        else:
                            nums[i] = nums[i+1]
                        break
                    else:
                        return False
                elif i+1 == ni:
                    nums[i+1] = nums[i]
                    break

        sorted_nums = sorted(nums)
        if nums == sorted_nums:
            return True
        else:
            return False


# nums = [5, 7, 1, 6]
# obj = Solution()
# res = obj.checkPossibility(nums)
# print(res)
