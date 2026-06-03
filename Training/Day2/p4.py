#Largest and 2nd largest element without using built in functions

#METHOD 1
l1=[1,3,6,8,2,5,99,4,23,45,21]
max1=l1[0]
max2=l1[0]
for i in range(1,len(l1)):
    if max2<l1[i]:
        prev=max2
        max2=l1[i]
        if max1<max2:
            max1=max2
            max2=prev
print(max1,max2)

#METHOD 2
max1=l1[0]
max2=l1[0]
for i in range(1,len(l1)):
    if max1<l1[i]:
        max2=max1
        max1=l1[i]
    elif l1[i]>max2 and l1[i]<max1:
        max2=l1[i]
print(max1,max2)
