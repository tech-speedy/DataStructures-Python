#    LinkedList =  Nodes are in 2 parts (data + address)
#                        Nodes are in non-consecutive memory locations
#                        Elements are linked using pointers
            
#    advantages?
#    1. Dynamic Data Structure (allocates needed memory while running)
#    2. Insertion and Deletion of Nodes is easy. O(1) 
#    3. No/Low memory waste
 
#    disadvantages?
#    1. Greater memory usage (additional pointer)
#    2. No random access of elements (no index [i])
#    3. Accessing/searching elements is more time consuming. O(n)
  
#    uses?
#    1. implement Stacks/Queues
#    2. GPS navigation
#    3. music playlist



#Implementing a linked list with an example

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

#Printing a linked list

current = node1
while current is not None:
    print(current.data, end = "->")
    current = current.next
print("None")
