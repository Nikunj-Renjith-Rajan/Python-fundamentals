# Given the head of a singly linked list, return the kth last element of the linked list.
class node:
    def __init__(self,u):
        self.data=u
        self.next=None
        
def insert(x):
    t=head
    while(t.next!=None):
        t=t.next
    t.next=node(x)

def kthlastval(head,k):
    f=s=head
    i=0
    while(i<k):
        f=f.next
        i+=1
    while(f.next!=None):
        f=f.next
        s=s.next
    return s.data

head=node(1)
insert(2)
insert(3)
insert(4)
insert(5)
insert(6)
insert(7)
k=2
print(kthlastval(head,k))