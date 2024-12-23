# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        swap=0
        q=deque()
        q.append(root)

        while q:
            qlen=len(q)
            res=[]

            for _ in range(qlen):
                node=q.popleft()
                res.append(node.val)

                if(node.left):
                    q.append(node.left)
                if(node.right):
                    q.append(node.right)
            
            sort_list=sorted(res)
            dic={}
            for i,v in enumerate(res):
                dic[v]=i
            
            for i in range(len(res)):
                if res[i]!=sort_list[i]:
                    swap+=1

                    curr = dic[sort_list[i]]
                    dic[res[i]]=curr
                    res[i],res[curr] = res[curr],res[i]
        return swap