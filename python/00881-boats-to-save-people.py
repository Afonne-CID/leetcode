class Solution(object):
    def numRescueBoats(self, people, limit):
        # Sort the people array in ascending order.
        people.sort()

        # Initialize pointers for the heaviest and lightest persons.
        right = len(people) - 1
        left = 0

        # Initialize the result to count the number of boats used.
        res = 0

        while left <= right:
            # Check if the sum of weights of the lightest and heaviest persons
            # does not exceed the boat's weight limit.
            if people[left] + people[right] <= limit:
                left += 1
            right -= 1

            # Increment the boat count.
            res += 1

        return res
