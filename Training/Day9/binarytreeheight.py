class node:
    def __init__(self,u):
        self.data=u
        self.left=None
        self.right=None

def height(root):
    if root==None:
        return -1
    else:
        return max(height(root.left),height(root.right))+1

root=node(10)
root.left=node(5)
root.right=node(1)
root.left.left=node(2)
root.left.right=node(3)
root.left.right.left=node(4)
root.left.right.right=node(2)
root.left.right.right.left=node(6)
root.left.right.right.right=node(8)
root.right.left=node(2)
root.right.left=node(7)
print("Height of the tree is ",end="")
print(height(root))