def isHappy(self, n: int) -> bool:
    slow, fast = n, self.sumSquareDigits(n)

    while slow != fast:
        fast = self.sumSquareDigits(fast)
        fast = self.sumSquareDigits(fast)
        slow = self.sumSquareDigits(slow)

    return True if fast == 1 else False
