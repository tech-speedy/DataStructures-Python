#Insertion at the beginning of Linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#Creating the nodes

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

#Connecting nodes to form a Linked List
node1.next = node2
node2.next = node3
node3.next = node4

#Creating a new node to insert

new_node = Node(25)

#Inserting the new node after the second node

current = node1
while current is not None and current.data != 20:
    current = current.next
new_node.next = current.next
current.next = new_node

#Printing a linked list

current = node1
while current is not None:
    print(current.data, end = " -> ")
    current = current.next
print("None")
