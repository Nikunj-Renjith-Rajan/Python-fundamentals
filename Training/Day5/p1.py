# new system    0 1 2 3 4 5 6 7 8 9 A B C....Z
# og System     0............................35
# Given n and k. Divide n by k until n is 0 and append all the remainders as string (in the new system) and reverse it and print it
def remrev(n,k):
    rem=0
    s=""
    while n>0:
        rem=n%k
        n=n//k
        if rem>35:
            return "Not possible"
        else:
            if rem<10:
                s=str(rem)+s
            else:
                s=chr(rem-10+65)+s
    return s

n=int(input("Read n:"))
k=int(input("Read k:"))
print(remrev(n,k))  