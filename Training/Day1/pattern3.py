#METHOD 1
n=int(input("Read limit:"))
for i in range (n):
    print(str(i+1)*(i+1))

#METHOD 2
for i in range (n):
    for j in range (i+1):
        print(i+1,end="")
    print("")

#METHOD 3
for i in range(n):
    print(int("1"*(i+1))*(i+1))

#METHOD 4
j=1
for i in range(n):
    print((i+1)*j)
    j=j*10+1

#METHOD 5
for i in range(n):
    print((10**(i+1)//9)*(i+1))

# Read limit:5
# 1 
# 22 
# 333 
# 4444 
# 55555 