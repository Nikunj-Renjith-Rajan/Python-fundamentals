#STRING COMPRESSION
# ip: aaaabbcccddddd
# op: a4b2c3d5
#ip:abcd
#op:abcd            because there is no point in compressing
s="aaaabbcccddddd"
s="abcd"
res=""
count=1
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        count+=1
    else:
        res+=s[i]+str(count)
        count=1
res+=s[i+1]+str(count)       #to print the last portion
count=1
if len(res)<len(s):
    print(res)
elif len(res)>=len(s):
    print(s)
        

    