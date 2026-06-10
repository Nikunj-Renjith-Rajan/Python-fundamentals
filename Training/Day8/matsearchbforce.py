# ip:5
# 2 3 5 1 6
# 4 5 6 7 3
# 8 9 2 1 4
# 5 3 6 7 9
# 2 9 8 6 3
# Find the occurence of ip and find its position in a square position
def find(n,mat,key):
    for i in range(n):
        for j in range(n):
            if mat[i][j]==key:
                return [i,j]
    return "Not found"

n=int(input("Read the matrix index:"))
mat=[]
print("Read the elements:")
for i in range(n):
        l=[]
        for j in range(n):
            k=int(input())
            l.append(k)
        mat.append(l)
key=int(input("Read the element to be found:"))
print(find(n,mat,key))



