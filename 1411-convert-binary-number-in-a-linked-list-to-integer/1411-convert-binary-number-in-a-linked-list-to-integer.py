# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        string=[]
        curr=head
        while curr is not None:
            string.append(str(curr.val))
            curr=curr.next
        ist=''.join(string)
        return  int(ist,2)