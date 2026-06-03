n=int(input("Read limit:"))
for i in range (n):
    for j in range (n-i):
        print("*",end=" ")
    print("")

# Read limit:5
# * * * * * 
# * * * * 
# * * * 
# * * 
# * 