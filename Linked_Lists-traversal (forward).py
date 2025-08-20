# Node class for Doubly Linked List
class Node:
    def __init__(self, data):
        self.data = data      # Data
        self.prev = None      # Pointer to previous node
        self.next = None      # Pointer to next node

# Doubly Linked List class
class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    # Function to append node at the end
    def append(self, data):
        new_node = Node(data)
        if self.head is None:   # If list is empty
            self.head = new_node
            return
        temp = self.head
        while temp.next:        # Traverse to last node
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp
    
    # Function for forward traversal
    def forward_traversal(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

# Example usage
dll = DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.append(30)
dll.append(40)

print("Forward Traversal:")
dll.forward_traversal()
