#Return the starting node of the cycle if there is a cycle in the linked list else return -1

# NOTES:
# The f and s pointers meet at a point in the cycle which depends on the number of non cycle nodes. 
# If there are 3 nodes before the cycle, then the 2 pointers will meet at 3 nodes before the starting point within the cycle
# So introduce one more pointer ,say t, and then t and s will meet at the starting point when jumped one at a time
class node:
    def __init__(self,u):
        self.data=u
        self.next=None
        
def insert(x):
    t=head
    while(t.next!=None):
        t=t.next
    t.next=node(x)

def cycleStart(head):
        f=s=head
        while f!=None and f.next!=None:
            f=f.next.next
            s=s.next
            if f==s:
                t=head
                while t!=s:
                    t=t.next
                    s=s.next
                return s.data
        return -1

head=node(10)
insert(20)
insert(10)
insert(40)      
insert(50)              #Assume there is a cycle to this node
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
print(cycleStart(head))

