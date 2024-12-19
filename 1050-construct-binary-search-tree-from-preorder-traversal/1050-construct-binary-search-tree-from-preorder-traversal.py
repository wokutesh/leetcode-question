# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if preorder is None:
            return None
        root=TreeNode(preorder[0])
        def insert(root:TreeNode,key)->TreeNode:
           
            if root is None:
                return TreeNode(key)
                
                

            if root.val<key:
                root.right=insert(root.right,key)
            if root.val >key:
                root.left=insert(root.left,key)
            return root

        for key in preorder:
            insert(root,key)

        return root