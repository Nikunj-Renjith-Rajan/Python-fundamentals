# Given the head of a singly linked list, reverse the list, and return the reversed list.
class node:
    def __init__(self,u):
        self.data=u
        self.next=None
        
def insert(x):
    t=head
    while(t.next!=None):
        t=t.next
    t.next=node(x)

def display(head):
    t=head
    while t!=None:
        print(t.data,end="")
        print("->",end="")
        t=t.next
    print("None")

def reverseList(head):
        p=None              #3 pointers-prev,current and next
        c=head
        n=c
        while n!=None:
            n=n.next
            c.next=p
            p=c
            c=n
        return p

head=node(10)
insert(20)
insert(10)
insert(40)      
insert(50)          
insert(60)
insert(70)
display(head)
display(reverseList(head))

        