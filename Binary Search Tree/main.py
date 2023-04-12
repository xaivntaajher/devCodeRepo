from linked_list import LinkedList
from binary_node import BinaryNode

class RunMain:
    def __init__(self):
        self.list = LinkedList()

    def append_nodes(self):
        print('Add a new node with the value of 5')
        self.list.append_node(5)
        print('Add a new node with the value of 10')
        self.list.append_node(10)
        print('Add a new node with the value of 55')
        self.list.append_node(55)

    def find_values(self):
        print('Search for a node with the value of 10')
        print(self.list.find_node(10))
        print('Search for a node with the value of 22')        
        print(self.list.find_node(22))


main = RunMain()
main.append_nodes()
main.find_values()

print()
print('Binary Tree: Insertion activity')
root = BinaryNode(27)
root.insert_node(14)
root.insert_node(35)
root.insert_node(10)
root.insert_node(19)
root.insert_node(31)
root.insert_node(42)
print()
print('Search for node with value of 31')
root.search_for_node(31)
print()
print('Search for node with value 11')
root.search_for_node(11)


