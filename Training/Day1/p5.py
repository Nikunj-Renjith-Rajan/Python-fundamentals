# count the prime number digits in a number
n=int(input("Read a number:"))
count=0
while(n>0):
    if n%10==2 or n%10==3 or n%10==5 or n%10==7:
        count+=1
    n=n//10
print(count)
