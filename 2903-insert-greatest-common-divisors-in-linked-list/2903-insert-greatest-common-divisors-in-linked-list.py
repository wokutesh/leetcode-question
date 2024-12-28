# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return
        curr = head
        while curr and curr.next:
            
            gcd_value = gcd(curr.val, curr.next.val)
            
          
            gcd_node = ListNode(val=gcd_value)
            
           
            gcd_node.next = curr.next
            curr.next = gcd_node
            
            
            curr = gcd_node.next
        
        return head

        