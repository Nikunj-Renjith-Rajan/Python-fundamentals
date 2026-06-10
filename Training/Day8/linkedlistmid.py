# Given the head of a singly linked list, return the middle node of the linked list.
# If there are two middle nodes, return the second middle node.
class node:
    def __init__(self,u):
        self.data=u
        self.next=None
        
def insert(x):
    t=head
    while(t.next!=None):
        t=t.next
    t.next=node(x)

def middleval(head):
    f=s=head               #f is the fast pointer and s is the slow pointer
    while f!=None and f.next!=None:
        f=f.next.next
        s=s.next
    return s.data
head=node(1)
insert(2)
insert(3)
insert(4)
insert(5)
insert(6)
insert(7)
print(middleval(head))