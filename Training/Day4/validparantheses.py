# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

def isValid(s):
        st=[]
        j=0
        for i in s:
            if i=='(' or i=='[' or i=='{':
                st.append(i)
            else:
                if not st:
                    return false
                if i==')' and st[-1]=='(' or i==']' and st[-1]=='[' or i=='}' and st[-1]=='{':
                    st.pop()
                else:
                    return False
        if len(st)==0:
            return True
        else:
            return False

s1="({})[]"
s2="{[}]"
print(isValid(s1))
print(isValid(s2))
        