a=int(input("Read a number:"))
s=0
while a>0:
    if(a%2==0):
        s=s+1
    a=a//10
print("Count of even digits:",s)