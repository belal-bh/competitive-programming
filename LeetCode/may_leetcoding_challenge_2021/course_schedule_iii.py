###### Accepted ######
import heapq


class Solution:
    def scheduleCourse(self, courses):
        h, t = [], 0
        for d, e in sorted(courses, key=lambda x: x[1]):
            if t+d <= e:
                t += d
                heapq.heappush(h, -d)
            elif h and -h[0] > d:
                t += d + heapq.heappop(h)
                heapq.heappush(h, -d)
        return len(h)


# courses = [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]
# obj = Solution()
# f = obj.scheduleCourse(courses)
# print(f)
