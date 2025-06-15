# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # If the tree is empty, return 0
        if root is None: 
            return 0

        # Use BFS with a queue: each element is [node, depth]
        queue = deque([[root, 1]])
        
        while queue:
            # Pop the front of the queue
            u, d = queue.popleft()

            # If the node is a leaf, return its depth
            if u.left is None and u.right is None:
                return d

            # Add children to the queue if they exist
            if u.left is not None:
                queue.append([u.left, d + 1])
            if u.right is not None:
                queue.append([u.right, d + 1])
        
        # Should never reach here
        return -1