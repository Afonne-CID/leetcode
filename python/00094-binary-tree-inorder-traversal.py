def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    # Initialize an empty list to store the result.
    res = []
    # Initialize an empty stack.
    stack = []
    cur = root

    while cur or stack:
        while cur:
            # Traverse left and push nodes onto the stack.
            stack.append(cur)
            cur = cur.left
        # Pop a node from the stack.
        cur = stack.pop()
        # Add the current node's value to the result.
        res.append(cur.val)
        # Move to the right subtree.
        cur = cur.right

    return res
