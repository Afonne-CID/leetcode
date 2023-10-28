def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
    # Create a set to keep track of valid positions in the target
    good = set()

    for t in triplets:
        # Check if any value in the triplet exceeds the corresponding target value
        if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
            continue
        # Check each position in the triplet
        for i, v in enumerate(t):
            # If the value matches the target, add the position to the set
            if v == target[i]:
                good.add(i)
    # If we can obtain all three target values, return true; otherwise, return false
    return len(good) == 3
