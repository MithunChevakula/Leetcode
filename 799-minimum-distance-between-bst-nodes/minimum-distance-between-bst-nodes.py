class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        flattened = []

        def dfs(node):
            if node is None:
                return
            dfs(node.left)
            flattened.append(node.val)
            dfs(node.right)

        dfs(root)
        ans = float("inf")
        for i in range(1, len(flattened)):
            ans = min(ans, flattened[i] - flattened[i - 1])
        return ans
    