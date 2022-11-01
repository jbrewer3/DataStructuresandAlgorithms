# define node class
class Node:
    #constructure with data value and .next value
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next 

class LinkedList:
    def __init__(self):
        self.head = None

    def insert():
        pass

    def delete():
        pass


n1 = Node(3) #creates node construct with value of 3 and next of none
n2 = Node(7)
n3 = Node(2)
n4 = Node(9)
        
LL = LinkedList() # we instantiated the ll class
LL.head = n1 #we identified that n1 is our head in ll

n1.next = n2
n2.next =  n3
n3.next = n4