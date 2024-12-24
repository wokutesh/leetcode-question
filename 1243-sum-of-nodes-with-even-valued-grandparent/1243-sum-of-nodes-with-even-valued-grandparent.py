# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 

        queue=deque([root])
        parent_map={root:None}
        grandparent_map={root:None}

        ans=0
        while queue:

            node=queue.popleft()

            if node.left:
                parent_map[node.left]=node
                grandparent_map[node.left]=parent_map[node]

                if grandparent_map[node.left] and grandparent_map[node.left].val % 2==0:
                    ans+=node.left.val

                queue.append(node.left)

            if node.right:
                parent_map[node.right]=node
                grandparent_map[node.right]=parent_map[node]

                if grandparent_map[node.right] and grandparent_map[node.right].val % 2==0:
                    ans+=node.right.val

                queue.append(node.right)

        return ans
