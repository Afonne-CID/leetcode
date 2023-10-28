def checkSubarraySum(nums, k):
    # Initialize a hashmap with one entry for the remainder 0 at index -1.
    # This handles the case where the subarray starts at index 0.
    hashmap = {0: -1}
    summ = 0

    for i, num in enumerate(nums):
        summ += num
        # Calculate the remainder of the current sum modulo k.
        current_remainder = summ % k

        # If the current remainder exists in the hashmap and the length of the subarray is at least 2, return True.
        if current_remainder in hashmap and i - hashmap[current_remainder] >= 2:
            return True

        # If the current remainder is not in the hashmap, add it with the current index.
        if current_remainder not in hashmap:
            hashmap[current_remainder] = i

    # If no valid subarray is found, return False.
    return False
