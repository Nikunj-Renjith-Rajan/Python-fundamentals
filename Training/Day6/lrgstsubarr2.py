# Given a string s, find the length of the longest substring without duplicate characters.

#METHOD 2 - O(n) Using dictionary
def lengthOfLongestSubstring(s):
        if(len(s)==0):
            return 0
        maxlen=0
        l=0
        r=0
        dic={}
        while r<len(s):
            if s[r] not in dic:
                dic[s[r]]=r
            else:
                if l<=dic[s[r]]:
                    l=dic[s[r]]+1
                dic[s[r]]=r
            maxlen=max(r-l+1,maxlen)      
            r+=1
        return maxlen
        
print(lengthOfLongestSubstring("abcabcabc"))
print(lengthOfLongestSubstring("bbbbb"))
print(lengthOfLongestSubstring("pwwkey"))
print(lengthOfLongestSubstring("abcdefghidklyzaxj"))