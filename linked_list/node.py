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
   
    def print_list(self):
        cur_node=self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next
    
    def deletion(self,data):
        current_node = self.head
        if data==self.head.data and current_node:
            self.head = current_node.next
            current_node = None
        prev_node = None
        while not current_node.data == data or current_node:
           prev_node = current_node
           current_node = current_node.next
        if current_node is None:
            print("Node Not Present")
            return 
        
        prev_node.next = current_node.next
        current_node = None

    def deletion_position(self,delete_position):
        
        current_node = self.head
        if delete_position==0:
            self.head = current_node.next
            current_node = None

        position=1
        prev_node = None
        while not position == delete_position or current_node:
           prev_node = current_node
           current_node = current_node.next
           position+=1
        if current_node is None:
            return 
        
        prev_node.next = current_node.next
        current_node = None
    
    def len_iterative(self):
        current_node = self.head
        count= 0
        while current_node:
            count+=1
            current_node = current_node.next
        return count
    def len_recursive(self,head_node):
        if head_node is None:
            return 0
        return 1+self.len_recursive(head_node.next)
    def node_by_key(self,key):
        cur_node = self.head
        pre_node = None
        while cur_node or not cur_node.data == key:
            pre_node = cur_node
            cur_node = cur_node.next
        return (pre_node,cur_node)
    def swap_node(self,key1,key2):
        pre_node_key1,cur_node_key1=self.node_by_key(key1)
        pre_node_key2,cur_node_key2=self.node_by_key(key2)
        if  not cur_node_key1 or not cur_node_key2:       
            return
        
        # SWAPPING PREVIOUS NODE POINTER
        if pre_node_key1:                         # CHecking if pre node exist
            pre_node_key1.next = cur_node_key2         
        else:                                     # Previous node for key1 is not present
            self.head = cur_node_key2   
        if pre_node_key2:                         # CHecking if pre node exist           
            pre_node_key2 = cur_node_key1
        else:                                     # Previous node for key2 is not present
            self.head = cur_node_key1
       
        # SWAPPING CURRENT NODE KEYS
        cur_node_key1.next,cur_node_key2.next = cur_node_key2.next,cur_node_key1.next