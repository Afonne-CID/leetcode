def subarraySum(nums, k):
    # Initialize variables for counting, current sum, and a hashmap.
    count = 0
    curr_sum = 0
    prefix_sum = {}

    # Initialize the prefix sum 0 with a count of 1 (base case).
    prefix_sum[0] = 1

    # Iterate through the array.
    for num in nums:
        curr_sum += num
        # Check if the difference between the current sum and k exists in prefix_sum.
        if curr_sum - k in prefix_sum:
            count += prefix_sum[curr_sum - k]

        # Update the prefix sum count or add it to the hashmap.
        prefix_sum[curr_sum] = prefix_sum.get(curr_sum, 0) + 1

    return count
