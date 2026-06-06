# Sort a list on the order of their length
a=["hello","car","a","apples","hi"] 
a.sort(key=len)             #Same for sorting a list of lists on the basis of list size
print(a)

#Sort a list on the order of sum,min and max of elements
a=[[6,7,2],[4,1,3,9],[17,8],[2],[8,2],[1,9]]
a.sort(key=sum)
print(a)

a=[[6,7,2],[4,1,3,9],[17,8],[2],[8,2],[1,9]]
a.sort(key=max)
print(a)

a=[[6,7,2],[4,1,3,9],[17,8],[2],[8,2],[1,9]]
a.sort(key=min)
print(a)





