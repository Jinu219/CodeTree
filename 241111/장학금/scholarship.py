middle,last = input().split(" ")
middle = int(middle)
last = int(last)
if( middle >= 90 and last >= 95):
    print(100000)
elif( middle >= 90 and last >= 90):
    print(50000)
else :
    print(0)