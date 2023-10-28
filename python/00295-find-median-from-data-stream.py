def findMedian(self) -> float:
    if len(self.small) > len(self.large):
        return -self.small[0]
    elif len(self.large) > len(self.small):
        return self.large[0]
    return (-self.small[0] + self.large[0]) / 2.0
