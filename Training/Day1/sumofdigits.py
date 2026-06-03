a=int(input("Read a number"))
s=0
while a>0:
    dig=a%10
    s=s+(a%10)
    a=a//10
print(s)