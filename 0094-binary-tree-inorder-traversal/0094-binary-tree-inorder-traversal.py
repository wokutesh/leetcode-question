# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode],arr=None) -> List[int]:
        if root is None:
            return []

        if arr is None:
            arr=[]

        self.inorderTraversal(root.left,arr)
        arr.append(root.val)
        self.inorderTraversal(root.right,arr)

        return arr

        