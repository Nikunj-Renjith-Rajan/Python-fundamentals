#Basics of linked list
class node:
    def __init__(self,u):
        self.data=u
        self.next=None
a=node(1)
b=node(2)
a.next=b
c=node(3)
b.next=c            #or a.next.next
print(a.data,end="->")
print(a.next.data,end="->")
print(a.next.next.data)
print(b.data)
print(b.next.data)
print(c.data)

# n=int(input("Read number of nodes:"))
# print("Read nodes:")
# head=int(input())
# a=head
# for i in range(1,n):
#     a=a.next
#     a=int(input())
t=a
while t!=None:
    print(t.data,end="")
    if t.next!=None:
        print("->",end="")
    t=t.next
