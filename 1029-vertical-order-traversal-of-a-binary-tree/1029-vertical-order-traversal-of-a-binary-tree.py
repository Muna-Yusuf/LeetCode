from collections import defaultdict, deque

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def verticalTraversal(self, root):
        if not root:
            return []
        
        column_table = defaultdict(list)
        queue = deque([(root, 0, 0)])

        while queue:
            node, row, col = queue.popleft()
            
            if node:
                column_table[col].append((row, node.val))
                queue.append((node.left, row + 1, col - 1))
                queue.append((node.right, row + 1, col + 1))

        sorted_columns = sorted(column_table.keys())
        result = []

        for col in sorted_columns:
            column_nodes = sorted(column_table[col], key=lambda x: (x[0], x[1]))
            result.append([val for row, val in column_nodes])

        return result