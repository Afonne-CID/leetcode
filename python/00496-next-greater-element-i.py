def nextGreaterElement(nums1, nums2):
    # Initialize a dictionary to map values to their indices in nums1
    nums1Idx = {n: i for i, n in enumerate(nums1)}
    # Initialize the result array with -1 values
    res = [-1] * len(nums1)

    stack = []
    for i in range(len(nums2)):
        cur = nums2[i]

        # While the stack exists and the current element is greater than the top of the stack
        while stack and cur > nums2[stack[-1]]:
            idx = stack.pop()
            if nums2[idx] in nums1Idx:
                res[nums1Idx[nums2[idx]]] = cur

        if cur in nums1Idx:
            stack.append(i)

    return res
