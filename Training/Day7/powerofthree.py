# Given an integer n, return true if it is a power of three. Otherwise, return false.
# An integer n is a power of three, if there exists an integer x such that n == 3**x.

import math
def isPowerOfThree(n):
        if n<=0:
            return False
        if n==1:
            return True
        if n%3==0:
            return isPowerOfThree(n//3)
        return False

print(isPowerOfThree(27))
print(isPowerOfThree(-21))
print(isPowerOfThree(0))

