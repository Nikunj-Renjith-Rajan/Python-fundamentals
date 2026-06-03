# Given a roman numeral, convert it to an integer

# Symbol       Value
#--------     --------
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

def romanToInt(s):
        dic={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        num=0
        flag=0
        for i in range(len(s)):
            if i!=len(s)-1 and dic[s[i]]<dic[s[i+1]] and flag!=1:
                flag=1
                x=dic[s[i]]
                continue
            elif flag!=1:
                num+=dic[s[i]]
            else:
                num+=(dic[s[i]]-x)
                flag=0
        return num    

print(romanToInt("LVIII"))
print(romanToInt("MCMXCIV"))    
    


        