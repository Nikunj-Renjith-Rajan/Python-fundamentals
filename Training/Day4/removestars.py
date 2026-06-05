# You are given a string s, which contains stars *.
# In one operation, you can:
# Choose a star in s.
# Remove the closest non-star character to its left, as well as remove the star itself.
# Return the string after all stars have been removed.

def removeStars(s):
        res=[]
        for i in range(0,len(s)):
            if s[i]!='*':
                res.append(s[i])
            else:
                res.pop()
        s="".join(res)
        return s

print(removeStars("lee**tco*de"))