class BinaryNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None
    
    def insert_node(self, data):
        node = BinaryNode(data)
        if data < self.data:
            if self.left == None:
                self.left = node
                print(f'Node with data {data} created, added to the node of {self.data} on the left side')
            else:
                self.left.insert_node(data)
        elif data > self.data:
            if self.right == None:
                self.right = node
                print(f'Node with data {data} created, added to the node of {self.data} on the right side')
            else:
                self.right.insert_node(data)
         
        
    def search_for_node(self, find_data):
        current_node = self
        while current_node != None:
            if current_node.data == find_data:
                print('Node found')
                return
            elif find_data < current_node.data:
                current_node = current_node.left
                print('Direction: Left')
            else:
                current_node = current_node.right
                print('Direction: Right')
                
        print('Node not found')          
            