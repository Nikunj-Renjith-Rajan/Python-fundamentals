# Find sum of all nodes and sum of all even nodes
class node:
    def __init__(self,u):
        self.data=u
        self.left=None
        self.right=None
    
def nodesum(root):
    if root==None:
        return 0
    else:
        return root.data+nodesum(root.left)+nodesum(root.right)

def evensum(root):
    if root==None:
        return 0
    else:
        if (root.data)%2==0:
            return root.data+evensum(root.left)+evensum(root.right)
        else:
            return evensum(root.left)+evensum(root.right)
        
root=node(10)
root.left=node(5)
root.right=node(15)
root.left.left=node(1)
root.left.right=node(8)
root.right.left=node(12)
print("Sum of all nodes:",end="")
print(nodesum(root))
print("Sum of all even nodes:",end="")
print(evensum(root))