#There are 2 lists, 1 is a list of characters charr and the other one is its priorities prarr. 
# Sort charr w.r.t prarr
def asd(x):
    return x[1]
l1=['f','d','a','z','x','q']
l2=[5,2,7,3,4,1]
l3=list(zip(l1,l2))
l3.sort(key=asd)
print(l3)