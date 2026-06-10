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
def nodesum(head):
    t=head
    s=0
    while t!=None:
        s+=t.data
        t=t.next
    return s
def middleval(head):                #This is the brute force approach
    t=head
    l=0
    while t!=None:
        t=t.next
        l+=1
    halflen=l//2
    t=head
    for i in range(halflen):
        t=t.next
    return t.data

head=node(1)
insert(2)
insert(3)
insert(4)
insert(5)
insert(6)
insert(7)
display(head)
print("Sum of nodes is ",nodesum(head))
print("Middle value is ",middleval(head))