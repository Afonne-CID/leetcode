def findDuplicate(nums):
    # Initialize slow and fast pointers
    slow, fast = 0, 0

    # Phase 1: Detect the intersection point of the two pointers
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]
        if slow == fast:
            break

    # Phase 2: Find the "entrance" to the cycle
    slow2 = 0
    while slow != slow2:
        slow = nums[slow]
        slow2 = nums[slow2]

    return slow
