# Given a pattern and a string s, find if s follows the same pattern.\

# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:
# 1.Each letter in pattern maps to exactly one unique word in s.
# 2.Each unique word in s maps to exactly one letter in pattern.
# 3.No two letters map to the same word, and no two words map to the same letter.
def wordPattern(pattern, s):
        dic={}
        l=s.split()
        if len(pattern)!=len(l):
            return False
        seen=set()
        for i in range(len(l)):
            if pattern[i] not in dic:
                if l[i] in seen:
                    return False
                dic[pattern[i]] = l[i]
                seen.add(l[i])
            else:
                if dic[pattern[i]]!=l[i]:
                    return False
        return True

print(wordPattern("abba","dog cat cat dog"))
print(wordPattern("abba","dog cat cat fish"))
print(wordPattern("abba","dog dog dog dog"))
        