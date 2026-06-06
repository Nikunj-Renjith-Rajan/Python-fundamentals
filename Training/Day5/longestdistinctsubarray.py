# Given a string s, find the length of the longest substring without duplicate characters.

def lengthOfLongestSubstring(s):
        if(len(s)==0):
            return 0
        maxlen=0
        l=0
        r=0
        cset=set()
        while r<len(s):
            if s[r] in cset:
                maxlen=max(r-l,maxlen)
                cset.remove(s[l])
                l+=1
            else:
                cset.add(s[r])
                maxlen=max(r-l+1,maxlen)
                r+=1
        return maxlen
        
print(lengthOfLongestSubstring("abcabcabc"))
print(lengthOfLongestSubstring("bbbbb"))
print(lengthOfLongestSubstring("pwwkey"))