class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        mincost = 0
        # print(costs)
        s1a = sorted(sorted(costs, key=lambda x: x[1], reverse=True), key=lambda x: x[0])
        s1 = sorted(s1a, key=lambda x: x[0]-x[1])
        print(s1)
        # s2a = sorted(sorted(costs, key=lambda x: x[0], reverse=True), key=lambda x: x[1])
        # s2 = sorted(s2a, key=lambda x: x[1]-x[0])
        # print(s2)
        s1_sum_a = 0
        s1_sum_b = 0
        n = len(costs)
        # s2_sum_a = 0
        # s2_sum_b = 0
        for i in range(n//2):
            s1_sum_a = s1_sum_a + s1[i][0]
            s1_sum_b = s1_sum_b + s1[n-i-1][1]
            # s2_sum_a = s2_sum_a + s2[i][1]
            # s2_sum_b = s2_sum_b + s2[n-i-1][0]
            
        total_s1_sum = s1_sum_a + s1_sum_b
        # total_s2_sum = s2_sum_a + s2_sum_b
        # print(total_s1_sum,total_s2_sum)
        # return min(total_s1_sum,total_s2_sum)
        return total_s1_sum
