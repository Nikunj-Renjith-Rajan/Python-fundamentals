# Tree basics - traversals and sum methods
class node:
    def __init__(self,u):
        self.data=u
        self.left=None
        self.right=None
    
def inorder(root):
    if root!=None:
        inorder(root.left)
        print(root.data,end=" ")
        inorder(root.right)

def preorder(root):
    if root!=None:
        print(root.data,end=" ")
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root!=None:
        postorder(root.left)
        postorder(root.right)
        print(root.data,end=" ")
    
root=node(10)
root.left=node(5)
root.right=node(15)
root.left.left=node(1)
root.left.right=node(8)
root.right.left=node(12)
print("INORDER : ",end="")
inorder(root)
print("")
print("PREORDER : ",end="")
preorder(root)
print("")
print("POSTORDER : ",end="")
postorder(root)
print("")
