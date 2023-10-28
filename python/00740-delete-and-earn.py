class Solution:
    def deleteAndEarn(self, nums):
        # Eliminate duplicates and count occurrences
        count = collections.Counter(nums)
        values = sorted(count.keys())

        # Initialize earn1 and earn2
        earn1, earn2 = 0, 0

        for value in values:
            # Calculate points for the current value
            points = value * count[value]

            # Check if the previous value is adjacent
            if value - 1 != values[-2]:
                earn1, earn2 = max(earn1, earn2) + points, earn1
            else:
                earn1, earn2 = earn2 + points, max(earn1, earn2)

        # Return the maximum points
        return max(earn1, earn2)
