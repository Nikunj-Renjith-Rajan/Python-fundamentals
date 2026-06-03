#a=[4,7,5,9,3,4]
#output->47 45 49 43 44 75 79 73 74 59.....
l1=[4,7,5,9,3,4]
for i in range(len(l1)-1):
    for j in range(i+1,len(l1)):
        print((l1[i]*10+l1[j]),end=" ")  #or print(l1[i],l1[j]),sep="",end=" ")