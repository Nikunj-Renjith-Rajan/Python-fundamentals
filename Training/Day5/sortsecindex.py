#Sort a list of lists on the order of its 2nd elements(i.e. index=1)
def asd(x):
    return x[1]
a=[[6,7,2],[4,1,3,9],[17,8],[8,2],[1,9]]
a.sort(key=asd)
print(a)
#OUTPUT: [[4, 1, 3, 9], [8, 2], [6, 7, 2], [17, 8], [1, 9]]
#             1             2       7           8       9