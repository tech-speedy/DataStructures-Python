#Deletion of an element at the end of the linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#Creating nodes

head = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

#Connecting nodes to form a linked list

head.next = node2
node2.next = node3
node3.next = node4

#Deleting the node from the end

current = head
while current.next.next is not None:
    current = current.next
current.next = None

#Printing the updated linked list

current = head
while current is not None:
    print(current.data, end="")
    if current.next is not None:
        print(" -> ", end="")
    current = current.next
