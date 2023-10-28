def getConcatenation(nums):
    ans = []  # Initialize an empty array to store the result
    for i in range(2):  # Iterate twice to concatenate the array
        for n in nums:
            ans.append(n)  # Append each element to the result
    return ans
