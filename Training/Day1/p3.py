# ip=6832
# sum=6**1 + 8**2 + 3**3 + 2**4
# dig=int(math.log(n,10)+1) to find number of digits
import math
n=int(input("Read a number:"))
i=int(math.log(n,10)+1)
sum=0
while (n>0):
    sum+=((n%10)**i)
    i-=1
    n//=10
print(sum)