# Write an algorithm to determine if a number n is happy.

# A happy number is a number defined by the following process:

# 1.Starting with any positive integer, replace the number by the sum of the squares of its digits.
# 2.Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# 3.Those numbers for which this process ends in 1 are happy.
# 4.Return true if n is a happy number, and false if not.

def isHappy(n):
        seen = set()
        while n > 1:
            if n in seen:
                return False            #looping infinitely
            seen.add(n)
            num = 0
            while n > 0:
                digit = n % 10
                num += digit ** 2  
                n = n // 10
            n = num
        return n == 1

n=int(input("Read a number:"))
print(isHappy(n))