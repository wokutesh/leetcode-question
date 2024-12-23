# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def deleteLeave(root,target):

            if root is None:
                return None
           
            root.left=deleteLeave(root.left,target)
            root.right=deleteLeave(root.right,target)

            if root.left is None and root.right is None and root.val==target:
                return None

            return root

        return deleteLeave(root,target)

        