# Ann has recently started commuting by subway. We know that a one ride subway ticket costs a rubles. 
# Besides, Ann found out that she can buy a special ticket for m rides (she can buy it several times). 
# It costs b rubles. Ann did the math; she will need to use subway n times. Help Ann, tell her what is 
# the minimum sum of money she will have to spend to make n rides?

# Input
# The single line contains four space-separated integers n, m, a, b (1 ≤ n, m, a, b ≤ 1000) — 
# the number of rides Ann has planned, the number of rides covered by the m ride ticket, 
# the price of a one ride ticket and the price of an m ride ticket.

# Output
# Print a single integer — the minimum sum in rubles that Ann will need to spend.
n=int(input("Read number of rides to be travelled:"))
m=int(input("Read number of rides included in the special ticket:"))
a=int(input("Read amount for 1 ride:"))
b=int(input("Read amount for special ticket:"))
res1=n*a
res2=((n//m)*b)+(a*(n%m))
res3=(n//m+1)*b
res=min(res1,res2,res3)
print(res)