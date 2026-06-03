#METHOD 1
n=int(input("Read limit:"))
for i in range (n):
    print("* "*(i+1))

#METHOD 2
n=int(input("Read limit:"))
for i in range (n):
    for j in range (i+1):
        print("*",end=" ")
    print("")

# Read limit:5
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 