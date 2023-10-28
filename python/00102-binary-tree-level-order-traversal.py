def levelOrder(self, root: TreeNode) -> List[List[int]]:
    res = []  # Initialize the result list
    q = collections.deque()  # Initialize a queue
    if root:
        q.append(root)  # Add the root node to the queue

    while q:
        val = []

        for i in range(len(q)):
            node = q.popleft()
            val.append(node.val)

            if node.left:
                q.append(node.left)

            if node.right:
                q.append(node.right)

        res.append(val)  # Add the values of this level to the result

    return res
