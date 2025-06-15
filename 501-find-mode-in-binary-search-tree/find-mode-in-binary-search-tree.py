# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node, freq):
            if(not node): return freq
            freq[node.val] = freq.get(node.val, 0) + 1
            freq = dfs(node.left, freq)
            freq = dfs(node.right, freq)
            return freq
        
        maxFreq = 0
        res = []
        for k, v in dfs(root, {}).items():
            if(v > maxFreq):
                res = [k]
                maxFreq = v
            elif(maxFreq == v):
                res.append(k)
        return res


        