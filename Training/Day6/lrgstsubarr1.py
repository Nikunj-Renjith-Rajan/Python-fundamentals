# Given a string s, find the length of the longest substring without duplicate characters.

#METHOD 1 - O(2n)
def lengthOfLongestSubstring(s):
        if(len(s)==0):
            return 0
        maxlen=0
        l=0
        r=0
        cset=set()
        while r<len(s):
            if s[r] in cset:
                cset.remove(s[l])
                l+=1
            else:
                cset.add(s[r])
                maxlen=max(r-l+1,maxlen)
                r+=1
        return maxlen
        
print("METHOD 1")
print(lengthOfLongestSubstring("abcabcabc"))
print(lengthOfLongestSubstring("bbbbb"))
print(lengthOfLongestSubstring("pwwkey"))
print(lengthOfLongestSubstring("abcdefghidklyzaxj"))

#METHOD 2 
def lengthOfLongestSubstring(s):
        if(len(s)==0):
            return 0
        maxlen=0
        l=0
        r=0
        cset=set()
        while r<len(s):
            if s[r] not in cset:
                cset.add(s[r])
                maxlen=max(r-l+1,maxlen)
            else:
                while(s[r] in cset):
                     cset.remove(s[l])
                     l+=1
                cset.add(s[r])
            r+=1
        return maxlen
print("METHOD 2")
print(lengthOfLongestSubstring("abcabcabc"))
print(lengthOfLongestSubstring("bbbbb"))
print(lengthOfLongestSubstring("pwwkey"))
print(lengthOfLongestSubstring("abcdefghidklyzaxj"))