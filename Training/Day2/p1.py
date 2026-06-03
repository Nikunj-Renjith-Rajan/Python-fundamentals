#List basics
a=[1]
print(a)
a.extend([2,3,4,5])         #appends the values in the list
print(a)
a.append([2,3,4,5])         #appends the list itself
print(a)
a.append(1)
print(a)
a.pop()
a.pop()
print(a)
a.insert(2,99)              #inserts 99 at 2nd pos
print(a)
a.remove(4)                 #removes 4 in the list
print(a)
del a           #deletes the entire list
