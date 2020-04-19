from linklist import LinkedList

    
def value_linklist(linklist):
    cur=linklist.head
    value = 0
    multiplier = 1
    while cur.next:
        value+= cur.data*multiplier
        multiplier*=10
        cur = cur.next
    return value
def add_linklists(list1,list2):
    return (value_linklist(list1)+value_linklist(list2))

