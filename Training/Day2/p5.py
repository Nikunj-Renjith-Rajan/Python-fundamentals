#PREFIX SUM
#----------
#input->[4,7,5,9,....]
#output->[4,11,16,25,....]
#res[i]=res[0]+res[1]+...+res[i]

l1=[4,7,5,9,3,4,2,9,3,8,1]
res=[]
sum=0
for i in l1:
    sum+=i
    res.append(sum)
print(res)