month = int(input())

# 1 3 5 7 8 10 12
if(month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
    print(31)
elif(month == 2):
    print(28)
else :
    print(30)