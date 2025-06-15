# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        sum_tilt = 0

        def postorder_dfs(node):
            nonlocal sum_tilt
            if node is None:
                return 0
            
            left_sum = postorder_dfs(node.left)
            right_sum = postorder_dfs(node.right)
            sum_tilt += abs(left_sum - right_sum)

            return node.val + left_sum + right_sum 

        postorder_dfs(root)
        return sum_tilt
    
        # O(n) time.
        # O(n) space.