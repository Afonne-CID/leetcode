def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    stack = [(root, False)]
    res = []

    while stack:
        cur, visited = stack.pop()

        if cur is None:
            continue

        if visited:
            res.append(cur.val)
        else:
            stack.append((cur, True))
            stack.append((cur.right, False))
            stack.append((cur.left, False))

    return res
