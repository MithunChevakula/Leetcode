class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        res = 0  
        while root:  
            if root.left:  
                # find the rightmost node (predecessor) in the left subtree of the current node.
                predecessor = root.left
                while predecessor.right and predecessor.right != root:
                    predecessor = predecessor.right
                
                # if no thread (temporary right link) exists back to the current node, create one
                if not predecessor.right:
                    predecessor.right = root  # temporary link 
                    root = root.left  
                else:
                    # a thread already exists, we are revisiting the node after exploring its left subtree
                    predecessor.right = None  
                    # check if predecessor is a left leaf
                    if predecessor == root.left and not predecessor.left:
                        res += predecessor.val 
                    root = root.right 
            else:
                root = root.right 
        return res

            