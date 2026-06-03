#List basics 2
a=[1,2,3,4,5,6]
print(len(a))               #size of list
print(max(a),min(a))        #min and max values
print(sum(a))               #sum of elements
print(*a)                   #print elements of the list
print(*a,sep=",")
for i in range(len(a)):
    print(a[i],end=" ")
for i in a:
    print(i,end=" ")