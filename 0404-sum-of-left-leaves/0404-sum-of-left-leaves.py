#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0
        
        left_leaves_sum = 0
        if root.left and not root.left.left and not root.left.right:
            left_leaves_sum += root.left.val  # Add left leaf's value
        
        # Recursively calculate the sum of left leaves for both children
        left_leaves_sum += self.sumOfLeftLeaves(root.left)
        left_leaves_sum += self.sumOfLeftLeaves(root.right)

        return left_leaves_sum
        
        