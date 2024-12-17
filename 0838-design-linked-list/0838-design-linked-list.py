class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        position = 0
        current_node = self.head
        while current_node:
            if index == position:
                return current_node.val
            current_node = current_node.next
            position += 1
        return -1

    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head
        self.head = new_node

    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val)
        if not self.head:  # If the list is empty
            self.head = new_node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0:  
            return
        new_node = ListNode(val)
        current_node = self.head
        position = 0
        if index == 0:  # Insert at the head
            new_node.next = self.head
            self.head = new_node
            return
        
        while current_node and position < index - 1:
            current_node = current_node.next
            position += 1


        if current_node:
            new_node.next = current_node.next
            current_node.next = new_node

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or not self.head:  # Handle edge case
            return
        if index == 0:  # Deleting the head
            self.head = self.head.next
            return
        
        current_node = self.head
        position = 0
        while current_node and position < index - 1:
            current_node = current_node.next
            position += 1

        if current_node and current_node.next:  
            current_node.next = current_node.next.next
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)