class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None  
    def append(self,data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return
        
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
<<<<<<< HEAD
        last_node.next = new_node  
=======
        last_node.next = new_node
    

    def insert_after(self,previous_node,data):
        if not previous_node:
            print("Previous node not in node")
            return
        new_node = Node(data)
        new_node.next = previous_node.next
        previous_node.next = new_node
   

    def prepend(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head = new_node

>>>>>>> a1afb2948d80e9d3e5d761a7b871ffa99ef580b5
    def print_list(self):
        cur_node=self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next  
    def deletion(self,data):
        cur_node = self.head
        if data==self.head.data and cur_node:
            self.head = cur_node.next
            cur_node = None
        prev_node = None
        while not cur_node.data == data and cur_node:
           prev_node = cur_node
           cur_node = cur_node.next
        if cur_node is None:
            print("Node Not Present")
            return 
        
        prev_node.next = cur_node.next
        cur_node = None
    def deletion_position(self,delete_position):
        
        cur_node = self.head
        if delete_position==0:
            self.head = cur_node.next
            cur_node = None

        position=1
        prev_node = None
        while not position == delete_position and cur_node:
           prev_node = cur_node
           cur_node = cur_node.next
           position+=1
        if cur_node is None:
            return 
        
        prev_node.next = cur_node.next
        cur_node = None   
    def len_iterative(self):
        cur_node = self.head
        count= 0
        while cur_node:
            count+=1
            cur_node = cur_node.next
        return count
    def len_recursive(self,head_node):
        if head_node is None:
            return 0
        return 1+self.len_recursive(head_node.next)
    def node_by_key(self,key):
        last_node = self.head
        pre_node = None
        while last_node and last_node.data == key:
            pre_node = last_node
            last_node = last_node.next
        return pre_node,last_node
    def swap_node(self,key1,key2):
        pre_node_key1,last_node_key1=self.node_by_key(key1)
        pre_node_key2,last_node_key2=self.node_by_key(key2)
        if  not last_node_key1 or not last_node_key2:       
            return
        
        # SWAPPING prev NODE POINTER
        if pre_node_key1:                         # CHecking if pre node exist
            pre_node_key1.next = last_node_key2         
        else:                                     # prev node for key1 is not present
            self.head = last_node_key2   
        if pre_node_key2:                         # CHecking if pre node exist           
            pre_node_key2 = last_node_key1
        else:                                     # prev node for key2 is not present
            self.head = last_node_key1
       
        # SWAPPING cur NODE KEYS
        last_node_key1.next,last_node_key2.next = last_node_key2.next,last_node_key1.next
    def reverse_list(self):
        prev = None
        cur = self.head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        self.head = prev
            
            
