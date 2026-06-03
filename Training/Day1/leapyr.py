y=int(input("Read yr:"))
if y%4==0:
    if y%100==0:
        if y%400:
            print("Leap yr")
        else:
            print("Not Leap yr")
    else:
        print("Leap yr")
else:
    print("Not leap yr")