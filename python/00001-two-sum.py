def twoSum(self, nums: List[int], target: int) -> List[int]:
    prev_nums = {}

    for index, value in enumerate(nums):
        diff = target – value
        if diff in prev_nums:
            return [index, prev_nums[diff]]
    prev_nums[value] = index
