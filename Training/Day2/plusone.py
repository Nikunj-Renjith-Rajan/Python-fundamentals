# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. 
# The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain 
# any leading 0's. Increment the large integer by one and return the resulting array of digits.

#METHOD 1
def plusOne1(digits):
        sum=0
        l=[]
        for i in digits:
            sum=sum*10+i
        sum+=1
        while sum>0:
            l.insert(0,sum%10)
            sum=sum//10
        return l

#METHOD 1
def plusOne2(digits):
        if(digits[-1]!=9):
             digits[-1]+=1
             return digits
        else:
            flag=0
            for i in range(len(digits)-1,-1,-1):
                    if digits[i]==9:
                        digits[i]=0
                    else:
                        digits[i]+=1
                        flag=1
                        break
            if flag==0:
                digits.insert(0,1)
            return digits

arr=[1,2,3]
print(plusOne1(arr))
print(plusOne2(arr))