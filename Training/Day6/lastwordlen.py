# Given a string s consisting of words and spaces, return the length of the last word in the string.
# A word is a maximal substring consisting of non-space characters only.
def lengthOfLastWord(s):
        flag=0
        l=0
        for i in range(len(s)-1,-1,-1):
            if not s[i].isalnum() and flag==1:
                break
            elif s[i].isalnum():
                l+=1
                flag=1
        return l

print(lengthOfLastWord("   fly me   to   the moon  "))
print(lengthOfLastWord("Hey hi hello"))
