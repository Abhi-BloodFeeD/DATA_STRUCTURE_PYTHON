
class Stack():
    
    def __init__(self):
        self.items = []
    
    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
    
    def get_stack(self):
        print(self.items)
    
    def is_empty(self):
        return self.items==[]
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
