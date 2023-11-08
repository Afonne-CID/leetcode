import math

def reverse(self, x: int) -> int:
    MIN = -2147483648  # Minimum 32-bit integer
    MAX = 2147483647  # Maximum 32-bit integer

    res = 0
    while x:
        digit = int(math.fmod(x, 10))  # Get the ones place digit
        x = int(x / 10)

        if res > MAX // 10 or (res == MAX // 10 and digit > MAX % 10):
            return 0
        if res < MIN // 10 or (res == MIN // 10 and digit < MIN % 10):
            return 0
        res = (res * 10) + digit

    return res
