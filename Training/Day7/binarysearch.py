def binsearch(l,r,key):
    if l<=r:
        mid=(l+r)//2
        if key>arr[mid]:
            return binsearch(mid+1,r,key)
        elif key<arr[mid]:
            return binsearch(l,mid-1,key)
        else:
            return True
    else:
        return False

arr=[1,3,4,5,7,11,15,27,56,83]
print(binsearch(0,len(arr)-1,2))
print(binsearch(0,len(arr)-1,5))