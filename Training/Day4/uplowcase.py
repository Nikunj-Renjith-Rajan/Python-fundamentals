# You are given a string word. A letter is called special if it appears both in lowercase and uppercase in word.
# Return the number of special letters in word.
def numberOfSpecialChars(word):
        charset=set(word)
        count=0
        for i in charset:
            if i.islower() and i.upper() in charset:
                count+=1
        return count

print(numberOfSpecialChars("aaBbCdc"))
print(numberOfSpecialChars("aaBeCd"))