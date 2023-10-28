def maxPathSum(root):
    result = [root.val]  # Store the result as a list for modification

    # Return the max path sum without splitting
    def dfs(root):
        if not root:
            return 0

        leftMax = dfs(root.left)
        rightMax = dfs(root.right)

        # Ensure negative values are not included in the path
        leftMax = max(leftMax, 0)
        rightMax = max(rightMax, 0)

        # Calculate max path sum WITH splitting the node
        result[0] = max(result[0], root.val + leftMax + rightMax)

        return root.val + max(leftMax, rightMax)

    dfs(root)
    return result[0]
