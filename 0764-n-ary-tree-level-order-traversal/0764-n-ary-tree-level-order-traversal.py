"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []

        res=[]
        queue=deque([root])

        while queue:
            arr=[]

            for _ in range(len(queue)):
                node=queue.popleft()
                arr.append(node.val)

                if node.children:
                    queue.extend(node.children)

            res.append(arr)

        return res
        