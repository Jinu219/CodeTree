year = int(input())

if(year % 4 == 0):
    if(year % 100 == 0 ):
        print("false")
    else :
        print("true")
else :
    print("false")