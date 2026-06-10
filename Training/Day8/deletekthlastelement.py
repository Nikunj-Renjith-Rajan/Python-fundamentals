# Given the head of a linked list, remove the nth node from the end of the list and return its head.
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

def kthlastvaldel(head,k):
    print("Before deletion")
    display(head)
    temp=node(0)                            #temp node is being introduced so that deletion of first node can be possible
    temp.next=head
    f=s=temp
    i=0
    while(i<k):                             #it is k instead of k-1 because we created a new node before head
        f=f.next
        i+=1
    while(f.next!=None):
        f=f.next
        s=s.next
    s.next=s.next.next
    print("After deletion")
    display(head)

head=node(1)
insert(2)
insert(3)
insert(4)
insert(5)
insert(6)
insert(7)
k=2
print(kthlastvaldel(head,k))