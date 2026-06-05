# You are given a license key represented as a string s that consists of only alphanumeric characters and dashes.
# The string is separated into n + 1 groups by n dashes. You are also given an integer k.
# We want to reformat the string s such that each group contains exactly k characters, except for the first group, 
# which could be shorter than k but still must contain at least one character. Furthermore, there must be a dash inserted 
# between two groups, and you should convert all lowercase letters to uppercase.

# Return the reformatted license key.

# Input: s = "5F3Z-2e-9-w", k = 4
# Output: "5F3Z-2E9W"
def licenseKeyFormatting(s, k):
        res=""
        s=s.upper()
        for j in range(len(s)):
            if s[j]!='-':
                res+=s[j]
            else:
                break
        if j==0:
            return ""
        s1=s.replace('-','')
        while j<len(s1)-1:
            res+="-"
            res+=s1[j:j+k]
            j+=k
        return res

print(licenseKeyFormatting("5F3Z-2e-9-w",4))
print(licenseKeyFormatting("2-5g-3-J",2))

        