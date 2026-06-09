#Generate the day for the entered date
def isleap(y):
    if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
        return 1
    return 0

def calcDate(d,m,y):
    oddday={0:'Sunday',1:'Monday',2:'Tuesday',3:'Wednesday',4:'Thursday',5:'Friday',6:'Saturday'}
    oddmonth={1:3,2:0,3:3,4:2,5:3,6:2,7:3,8:3,9:2,10:3,11:2,12:3}
    if isleap(y):
        oddmonth[2] = 1
    odd=0
    y-=1
    x1=y%400
    century=x1//100
    if century==1:
        odd+=5
    elif century==2:
        odd+=3
    elif century==3:
        odd+=1
    x2 = x1 % 100
    ly=x2//4 
    ny=x2-ly
    odd+=(ly*2)+ny
    for i in range(1,m):
        odd+=oddmonth[i]
    odd+=(d%7)
    odd=odd%7
    return oddday[odd]

d=int(input("Read the date:"))
m=int(input("Read the month number:"))
y=int(input("Read the year:"))
print(f"{d}/{m}/{y} : {calcDate(d, m, y)}")



