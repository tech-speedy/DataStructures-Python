# Linked List is a self referencial data structure
# A structure that has a variable that points the same structure as its own and is the same type.

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

#Adding a new node at the beginning

head = node1
new_node = Node(50)
new_node.next = head
head = new_node

#Function to print the linked list

def print_list(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

# Call the print function

print_list(head)
