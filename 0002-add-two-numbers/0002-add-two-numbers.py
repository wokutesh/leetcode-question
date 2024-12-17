# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        string1=''
        string2=''
        while l1:
            string1+=str(l1.val)
            l1=l1.next
        while l2:
            string2+=str(l2.val)
            l2=l2.next

        rev_str1=string1[::-1]
        rev_str2=string2[::-1]

        result=int(rev_str1)+int(rev_str2)
        s=str(result)
        target=None
        for i in range(len(s)):
            target=ListNode(val=int(s[i]),next=target)

        return target       