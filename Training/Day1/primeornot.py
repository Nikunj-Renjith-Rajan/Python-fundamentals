import math
a=int(input("Read a number:"))
if a==0 or a==1:
    flag=0
flag=1
for i in range (2,int(math.sqrt(a))+1):
    if  a%i==0:
        flag=0
        break
if flag==0:
    print("Not Prime")
else:
    print("Prime")