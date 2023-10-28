def tree2str(root):
    # Initialize an empty list to store the result
    result = []

    # Define a helper function for preorder traversal
    def preorder(node):
        if not node:
            return
        result.append(str(node.val))
        if node.left or node.right:
            result.append('(')
            preorder(node.left)
            result.append(')')
        if node.right:
            result.append('(')
            preorder(node.right)
            result.append(')')

    # Start the preorder traversal from the root
    preorder(root)

    # Join the result list into a single string
    return ''.join(result)
