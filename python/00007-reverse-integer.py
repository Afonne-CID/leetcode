class Solution:
    def reverse(self, x: int) -> int:
        MAX = 2**31 – 1 # Maximum 32-bit integer

        res = 0
        sign = 1
        if x < 0:
            sign = -1
            x = abs(x)

        while x:
            digit, x = x % 10, x // 10
            if res > MAX // 10 or (res == MAX // 10 and digit > MAX % 10):
                return 0
            res = (res * 10) + digit

        return res * sign
