import heapq as hp


class Solution:
    def isPossible(self, target):
        h = [-num for num in target]
        t = sum(target)
        hp.heapify(h)

        while -h[0] != 1:
            num = -hp.heappop(h)
            t -= num
            if num <= t or t < 1:
                return False
            num %= t
            t += num
            hp.heappush(h, -num)
        return True


# target = [3, 58, 33]
# obj = Solution()
# res = obj.isPossible(target)
# print(res)
