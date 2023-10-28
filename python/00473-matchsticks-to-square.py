def makesquare(matchsticks):
    # Calculate the target side length of the square
    length = sum(matchsticks) // 4
    sides = [0] * 4  # Initialize four sides with zero length

    # If the total sum of matchsticks is not divisible by 4, it's impossible to form a square
    if sum(matchsticks) % 4 != 0:
        return False

    # Sort matchsticks in descending order to prioritize larger matchsticks
    matchsticks.sort(reverse=True)

    # Backtracking function to find a valid placement of matchsticks
    def backtrack(i):
        if i == len(matchsticks):
            return True

        for j in range(4):
            if sides[j] + matchsticks[i] <= length:
                sides[j] += matchsticks[i]
                if backtrack(i + 1):
                    return True
                sides[j] -= matchsticks[i]
        return False

    return backtrack(0)
