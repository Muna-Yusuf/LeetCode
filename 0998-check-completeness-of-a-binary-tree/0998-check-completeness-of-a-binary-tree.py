# Definition for a binary tree node.
from collections import deque
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isCompleteTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root:
            return True
        
        queue = deque([root])
        end_tree = False

        while queue:
            node = queue.popleft()
            if node:
                if end_tree:
                    return False
            # Enqueue left and right children
                queue.append(node.left)
                queue.append(node.right)
            else:
                end_tree = True
        return True