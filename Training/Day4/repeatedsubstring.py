# Given a string s, check if it can be constructed by taking a substring of it
# and appending multiple copies of the substring together.
def repeatedSubstringPattern(s):
        st=s+s
        if s in st[1:-1]:
            return True
        else:
            return False
    
s=input("Read a string")
print(repeatedSubstringPattern(s))
        