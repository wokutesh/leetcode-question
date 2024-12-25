# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:

        if root is None:
            return

        queue=deque([root])
        temp=set()
        while queue:

            for _ in range(len(queue)):
                node=queue.popleft()

                temp.add(node.val)

                if node.left:
                    node.left=queue.append(node.left)
                if node.right:
                    node.right=queue.append(node.right)

        if len(temp)==1:
            return True
        else:
            return False

        