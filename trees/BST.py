class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None 

class BST:
    def __init__(self):
        self.root = None

    #Inserting into the BST

    def insert(self, value):
        new_node = Node(value)

        if self.root is None:
            self.root = new_node
            return

        current = self.root

        #the main insertion starts here 

        while True:
            #the left comparison 
            if value < current.value:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left
                #the right comparison 
            else:
                if value > current.value:
                    if current.right is None:
                        current.right = new_node
                        return
                    current = current.right

# Create tree
tree = BST()

# Insert values
tree.insert(10)
tree.insert(5)
tree.insert(15)
tree.insert(3)
tree.insert(7)
tree.insert(12)
tree.insert(18)























