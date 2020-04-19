class Node():
    def __init__(self):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None
    
    def append(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    
    def insert_after(self,previous_node,data):
        if not previous_node:
            print("Previous node not in node")
            return
        new_node = Node(data)
        new_node.next = previous_node.next
        previous_node.next = new_node
   
    def print_list(self):
        cur_node=self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next