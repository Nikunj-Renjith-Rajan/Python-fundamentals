# CODE IS WRONG FOR MISSING ELEMENTS-CORRECT IT

#Using binary search find the index of first occuring key. If element not found display -1
def binsearchfirstoccur(l,r,key,res):
    if l<=r:
        mid=(l+r)//2
        if key>arr[mid]:
            return binsearchfirstoccur(mid+1,r,key,res)
        elif key<arr[mid]:
            return binsearchfirstoccur(l,mid-1,key,res)
        else:
            res=mid
            return binsearchfirstoccur(l,mid-1,key,res)
    else:
        return res

#Using binary search find the index of last occuring key. If element not found display -1 
def binsearchlastoccur(l,r,key,res):
    if l<=r:
        mid=(l+r)//2
        if key>arr[mid]:
            return binsearchlastoccur(mid+1,r,key,res)
        elif key<arr[mid]:
            return binsearchlastoccur(l,mid-1,key,res)
        else:
            res=mid
            return binsearchlastoccur(mid+1,r,key,res)
    else:
        return res

arr=[1,2,3,3,3,3,7,7,9,12]
print(binsearchfirstoccur(0,len(arr)-1,3,-1))
print(binsearchlastoccur(0,len(arr)-1,3,-1))