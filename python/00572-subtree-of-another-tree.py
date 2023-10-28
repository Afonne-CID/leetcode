class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
    if not t:
        return True
    if not s:
        return False

    if self.sameTree(s, t):
        return True

    return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
