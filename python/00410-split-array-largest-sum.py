def splitArray(nums, k):
    def canSplit(largest):
        subarray = 1
        curSum = 0
        for n in nums:
            curSum += n
            if curSum > largest:
                subarray += 1
                curSum = n
        return subarray <= k

    left, right = max(nums), sum(nums)
    result = right

    while left <= right:
        mid = left + ((right - left) // 2)
        if canSplit(mid):
            result = mid
            right = mid - 1
        else:
            left = mid + 1

    return result
