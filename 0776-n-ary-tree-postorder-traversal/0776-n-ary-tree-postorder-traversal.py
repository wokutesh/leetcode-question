"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node',arr=None) -> List[int]:
        if root is None:
            return []
        
        if arr is None:
            arr=[]

        for child in root.children :
            self.postorder(child,arr)

        arr.append(root.val)

        return arr
