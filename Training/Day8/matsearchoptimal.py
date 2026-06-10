#Input is a sorted square matrix
def find(n,mat,key):
      l=0
      r=(n*n)-1
      while l<=r:
            mid=(l+r)//2
            if mat[mid//n][mid%n]<key:
                  l=mid+1
            elif mat[mid//n][mid%n]>key:
                  r=mid-1
            else:
                  return [mid//n,mid%n]
      return "Not Found"
                  
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