class Solution:
    memo = {}

    def tribonacci(self, n: int) -> int:
        if n in self.memo:
            return self.memo[n]
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        self.memo[n] = (
            self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)
        )
        return self.memo[n]
