def guessNumber(self, n: int) -> int:
    # Initialize the left and right boundaries
    left = 1
    right = n

    while True:
        # Calculate the midpoint
        mid = left + (right - left) // 2

        # Use the guess function to determine the next step
        result = guess(mid)

        if result == 1:
            # Our guess is lower than the chosen number
            left = mid + 1
        elif result == -1:
            # Our guess is higher than the chosen number
            right = mid - 1
        else:
            # We found the correct number
            return mid
