# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def dfs(original_tree,cloned_tree, target):
            if original_tree is None:
                return None
            
            
            if original_tree == target:
                return cloned_tree 
         
            left = dfs(original_tree.left,cloned_tree.left, target)
            right = dfs(original_tree.right,cloned_tree.right, target)

    
            return left or right

        return dfs(original,cloned, target)