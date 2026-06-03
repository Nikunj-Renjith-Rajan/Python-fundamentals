#Find the sum and count of odd and even numbers from the list
l1=[7,5,6,3,4,2,3,6,1]
esum=0
ecount=0
osum=0
ocount=0
for i in l1:
    if i%2==0:
        esum+=i
        ecount+=1
    else:
        osum+=i
        ocount+=1
print(esum,osum)
print(ecount,ocount)