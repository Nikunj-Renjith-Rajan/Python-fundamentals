#CONSTRAINTS
# pswd length>=8
# At least 1 uppercase,1 lowercase,1 digit,1 spcl char
# If not valid tell the user how many more type of characters are to be added to make the program valid

def pswdmngr(s):
    u=0
    l=0
    sp=0
    d=0
    for i in range(len(s)):
        if s[i].isupper():
            u=1
        elif s[i].islower():
            l=1
        elif s[i].isdigit():
            d=1
        else:
            sp=1
    missing=4-(u+l+sp+d)
    l=8-len(s)
    if u!=0 and l!=0 and d!=0 and sp!=0 and len(s)>=8:
        print("VALID")
    else:
        print("INVALID")
        print("Need more ",max(missing,l)," characters")
s=input("Read your password:")
pswdmngr(s)
