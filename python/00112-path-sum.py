def hasPathSum(self, root, targetSum):
    if not root:
        return False

    # Create a stack to store tuples of nodes and their corresponding remaining sums.
    stack = [(root, targetSum - root.val)]

    while stack:
        node, current_sum = stack.pop()

        # If we reach a leaf node and the sum equals the targetSum, return True.
        if not node.left and not node.right and current_sum == 0:
            return True

        # Explore the right subtree if it exists and update the remaining sum.
        if node.right:
            stack.append((node.right, current_sum

 - node.right.val))

        # Explore the left subtree if it exists and update the remaining sum.
        if node.left:
            stack.append((node.left, current_sum - node.left.val))

    # If no valid path is found, return False.
    return False
