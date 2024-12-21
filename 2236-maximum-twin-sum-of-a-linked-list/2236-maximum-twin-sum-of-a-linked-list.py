# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        max_val=0
        
        if head is None:
            return 
        if head and head.next is None:
            return head
        curr=head
        arr=[]
        while curr:
            arr.append(curr.val)
            curr=curr.next
        n=(len(arr)//2)-1
        for i in range(n+1):
            sum_val=arr[i]+arr[len(arr)-1-i]
            max_val=max(max_val,sum_val)

        return max_val

        