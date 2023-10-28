def partitionLabels(self, S: str) -> List[int]:
    count = {}
    res = []
    i, length = 0, len(S)

    # Build a hashmap to store the last occurrence index of each character in the string
    for j in range(length):
        c = S[j]
        count[c] = j

    curLen = 0
    goal = 0

    # Iterate through the string
    while i < length:
        c = S[i]
        goal = max(goal, count[c])
        curLen += 1

        # If the goal is reached (end of the current partition), add the length to the result
        if goal == i:
            res.append(curLen)
            curLen = 0
        i += 1

    return res
