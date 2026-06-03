# ip=6832
# sum=6**4 + 8**3 + 3**2 + 2**1
n=int(input("Read a number:"))
i=1
sum=0
while (n>0):
    sum+=((n%10)**i)
    i+=1
    n//=10
print(sum)