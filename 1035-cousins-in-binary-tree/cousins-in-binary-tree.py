# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        stack = [(root,None,0)]
        ret = []
        while stack:
            node,parent,depth = stack.pop()
            if node.val==x or node.val==y:
                ret.append((node,parent,depth))
            if node.right: stack.append((node.right,node,depth+1))
            if node.left: stack.append((node.left,node,depth+1))

        nodex,nodey = ret
        node1,parent1,depth1 = nodex
        node2,parent2,depth2 = nodey
        return depth1==depth2 and parent1!=parent2