def productExceptSelf(self, nums: List[int]) -> List[int]:
    # Calculate the prefix products
    n = len(nums)
    prefix_products = [1] * n
    prefix_product = 1
    for i in range(n):
        prefix_products[i] = prefix_product
        prefix_product *= nums[i]

    # Calculate postfix products and populate the answer array
    postfix_product = 1
    answer = [0] * n  # Initialize the answer array
    for i in range(n – 1, -1, -1):
        answer[i] = prefix_products[i] * postfix_product
        postfix_product *= nums[i]

    return answer
