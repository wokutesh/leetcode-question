# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:

        if root is None:
            return

        queue=deque([root])

        while queue:
            arr=[]

            for _ in range(len(queue)):
                node=queue.popleft()
                arr.append(node.val)

                if node.left:
                    node.left=queue.append(node.left)
                if node.right:
                    node.right=queue.append(node.right)

        return arr[0]       