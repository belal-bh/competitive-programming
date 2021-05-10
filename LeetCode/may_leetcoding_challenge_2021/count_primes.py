class Solution:
    def countPrimes(self, n):
        is_primes = [True]*n
        for i in range(2, int(n**0.5)+1):
            if is_primes[i]:
                is_primes[i*i:n:i] = [False]*((n-1)//i - i + 1)
        return sum(is_primes[2:])


# n = int(input())  # 111
# obj = Solution()
# res = obj.countPrimes(n)
# print(res)
