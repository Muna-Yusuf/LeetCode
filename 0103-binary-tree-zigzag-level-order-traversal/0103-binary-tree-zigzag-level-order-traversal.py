# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []  # If the tree is empty, return an empty list
        
        from collections import deque
        
        result = []
        queue = deque([root])
        left_to_right = True
        
        while queue:
            level_size = len(queue) 
            level_nodes = []
            
            for _ in range(level_size):
                node = queue.popleft()
                
                level_nodes.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if not left_to_right:
                level_nodes.reverse()
                
            result.append(level_nodes)
            left_to_right = not left_to_right
        
        return result