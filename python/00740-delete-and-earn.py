class Solution:
    def deleteAndEarn(self, nums):
        if not nums:
            return 0

        # Eliminate duplicates and count occurrences
        count = collections.Counter(nums)
        max_num = max(count.keys())  # Determine the maximum value in the 'count' dictionary
        
        # Create a list to store the earned points for each value
        dp = [0] * (max_num + 1)

        # Initialize dp[1] and dp[2]
        dp[1] = count[1] * 1
        if max_num > 1:
            dp[2] = max(count[1] * 1, count[2] * 2)

        for i in range(3, max_num + 1):
            # Calculate points for the current value
            points = i * count[i]

            # Update dp[i] using the previous values in dp
            dp[i] = max(dp[i - 2] + points, dp[i - 1])

        # Return the maximum points
        return dp[max_num]

