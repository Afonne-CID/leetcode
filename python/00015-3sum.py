def threeSum(self, nums: List[int]) -> List[List[int]]:

    # Sort the input array
    nums.sort()
    result = []
    
    # Iterate through the array
    for i in range(len(nums) – 2):
        # Skip duplicates
        if i > 0 and nums[i] == nums[i – 1]:
            continue
        
        # Initialize two pointers
        left, right = i + 1, len(nums) – 1
        
        while left < right:
            three_sum = nums[i] + nums[left] + nums[right]
            
            if three_sum > 0:
                right -= 1
            elif three_sum < 0:
                left += 1
            else:
                # Found a triplet
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                
                # Skip duplicates
                while left < right and nums[left] == nums[left – 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
    
    return result
