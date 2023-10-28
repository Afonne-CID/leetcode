class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None

        # The first value in preorder is the root.
        root = TreeNode(preorder[0])

        # Find the index of the root value in inorder.
        mid = inorder.index(preorder[0])

        # Recursively construct the left and right subtrees.
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])

        return root
