
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
