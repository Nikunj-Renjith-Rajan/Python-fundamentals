#input:seconds
#output:hr mins secs
time=int(input("Read time in seconds:"))
hrs=time//3600
mins=time%3600//60
secs=time%3600%60                                           #which is the same as time%60
print(hrs," Hours ",mins," Minutes ",secs," secs ")