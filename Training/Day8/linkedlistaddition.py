# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, 
# and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# EXAMPLE:
# input: 2->4->3
#        5->6->4
# output:7->0->8              (342+465=807)
class node:
    def __init__(self,u):
        self.data=u
        self.next=None

def insert(head,x):
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
    print("None",end="")
    
def addTwoNumbers(l1,l2):
        dummy=node(0)
        current=dummy
        c=0  
        while l1 or l2 or c:
            val1=l1.data if l1 else 0
            val2=l2.data if l2 else 0
            total=val1+val2+c
            c=total//10
            current.next=node(total%10)
            current=current.next
            if l1!=None:
                l1=l1.next
            if l2!=None:
                l2=l2.next
        return dummy.next

head1=node(2)
insert(head1,4)
insert(head1,3)
head2=node(5)
insert(head2,6)
insert(head2,4)
print("The Sum of ",end="")
display(head1)
print(" and ",end="")
display(head2)
print(" is ",end="")
display(addTwoNumbers(head1,head2))

