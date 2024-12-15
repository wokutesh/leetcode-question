# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None and head.next is None:
            return True

        map=[]
        curr=head
        while curr:
            map.append(curr.val)
            curr=curr.next
        curr=head
        while curr and curr.val==map.pop():
            curr=curr.next

        return curr is None
       


