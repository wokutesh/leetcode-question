# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode],arr=None) -> List[int]:
        if arr is None:
            arr=[]
        if root is None:
            return arr
        arr.append(root.val)
        self.preorderTraversal(root.left,arr)
        self.preorderTraversal(root.right,arr)
        return arr