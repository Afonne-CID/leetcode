def containsDuplicate(nums):
    # Initialize an empty hash set
    num_set = set()
    
    # Iterate through the elements in the array
    for num in nums:
        # Check if the current element is already in the set
        if num in num_set:
            return True  # Found a duplicate
        # Add the current element to the set
        num_set.add(num)
    
    # If we reach this point, no duplicates were found
    return False
