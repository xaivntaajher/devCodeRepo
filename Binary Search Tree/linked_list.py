# Create a linked list with the following functionality:
# append_node
# Add a node to the tail of the Linked List.
# find_node
# Given a value, search the Linked List until you find it. If you find it,
# return the boolean value True. Otherwise, return the boolean value False.


class Node:
    def __init__(self, data) -> None:
        self.next = None
        self.data = data

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        
    def append_node(self,data):
        node = Node(data)

        if self.head == None:
            self.head = node
                   
        else:
            current_node = self.head
            if current_node.next == None:
                current_node.next = node
            
    def find_node(self,find_data):
        current_node = self.head
        while current_node != None:
            if current_node.data == find_data:
                return True
            else:
                current_node = current_node.next
        return False
