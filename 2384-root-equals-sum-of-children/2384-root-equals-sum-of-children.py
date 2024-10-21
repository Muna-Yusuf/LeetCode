# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def checkTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root:
            return False
        
        left_value = root.left.val if root.left else 0
        right_value = root.right.val if root.right else 0

        return root.val == (left_value + right_value)

        