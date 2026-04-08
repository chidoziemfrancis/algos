class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    
    #add to the linked list 

    def append(self, value):
        new_node = Node(value)

        #we check if the head is empty then assign the first data 

        if self.head is None:
            self.head = new_node
            return

        #if the head is not empty 

        last = self.head

        while last.next:
            last = last.next
        
        last.next = new_node


    #tranversing a linkedlist 

    def display (self):
        current = self.head 
        
        while current:
            print(current.data, end= " -> ")
            current = current.next
        print("None")


#Example 

chat = LinkedList()

chat.append("Hi")
chat.append("How are you?")
chat.append("Good")

chat.display()