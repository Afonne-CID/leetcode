def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
    # Base case: If the tree is empty, create a new node with the given value.
    if not root:
        return TreeNode(val)

    # Use a pointer to keep track of the current node.
    cur = root

    while True:
        if val < cur.val:
            if not cur.left:
                cur.left = TreeNode(val)
                break
            else:
                cur = cur.left
        else:
            if not cur.right:
                cur.right = TreeNode(val)
                break
            else:
                cur = cur.right

    return root
