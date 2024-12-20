"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node',arr=None) -> List[int]:
        
        if root is None:
            return []

        if arr is None:
            arr=[]
        arr.append(root.val)
        for child in root.children or []:
            self.preorder(child,arr)

      

        return arr