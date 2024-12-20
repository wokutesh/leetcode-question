# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return 

        
        level = 1
        queue = deque([root])

        while queue:
            arr = []
            size = len(queue)
            
            for _ in range(size):
                node = queue.popleft()
                arr.append(node)
                
               
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if level % 2== 0: 
                values = [node.val for node in arr]
                reversed_val = values[::-1]

                for i, node in enumerate(arr):
                    node.val = reversed_val[i]
            
            level += 1 

        return root