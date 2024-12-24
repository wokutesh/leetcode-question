# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        if root is None:
            return []

        result=[]

        queue=deque([root])
        while queue:
            arr=[]

            for i in range(len(queue)):
                node=queue.popleft()

                arr.append(node.val)

                if node.left:
                    node.left=queue.append(node.left)

                if node.right:
                    node.right=queue.append(node.right)
            result.append(sum(arr)/len(arr))
            
                

        

        return result
        