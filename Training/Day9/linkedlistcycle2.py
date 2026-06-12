#Return the number of nodes if there is a cycle in the linked list else return -1
class node:
    def __init__(self,u):
        self.data=u
        self.next=None
        
def insert(x):
    t=head
    while(t.next!=None):
        t=t.next
    t.next=node(x)

def hasCycle(head):
        f=s=head
        while f!=None and f.next!=None:
            f=f.next.next
            s=s.next
            if f==s:
                s=s.next
                c=1
                while f!=s:
                     s=s.next
                     c+=1
                return c
        return -1

head=node(10)
insert(20)
insert(10)
insert(40)      
insert(50)          #Assume there is a cycle to this node
insert(60)
insert(70)
insert(80)
insert(90)
insert(100)
t=head
while(t.next!=None):            #Creating the cycle
        t=t.next
p=head
for i in range(4):
     p=p.next
t.next=p
print(hasCycle(head))

