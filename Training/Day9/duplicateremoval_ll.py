# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. 
# Return the linked list sorted as well.
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

def deleteDuplicates(head):
        curr=head
        while curr!=None and curr.next!=None:
            if curr.data==curr.next.data:
                curr.next=curr.next.next
            else:
                curr=curr.next
        return head

head=node(1)
insert(1)
insert(2)
insert(3)      
insert(4)          #Assume there is a cycle to this node
insert(4)
insert(7)
insert(9)
insert(9)
insert(9)
display(head)
print("Removing all duplicates.........")
display(deleteDuplicates(head))
