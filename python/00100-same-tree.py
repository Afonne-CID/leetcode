class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # Base cases
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False

        # Recursive step
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
