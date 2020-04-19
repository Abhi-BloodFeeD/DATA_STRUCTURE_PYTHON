from linklist import LinkedList

def palindrome(linked_list):
    cur = linked_list.head
    sur = linked_list.head

    s=[]
    isTrue = True
    while sur:
        s.append(sur.data)   
        sur=sur.next
    for elements in s[::-1]:
        if elements == cur.data:
            cur=cur.next
        else:
            return False    
    return True


            