# Extract the unique integers from the string and find the largest permutation possible from it
ip="fr4f5jwoier72984yhkj23g5923"
s = {i for i in ip if i.isdigit()}
l = list(s)
l.sort(reverse=True)
print(*l,sep="")
