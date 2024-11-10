a,b,c = input().split(" ")
a = int(a)
b = int(b)
c = int(c)

if ( a <= b and a <= c ):
    result = a
elif ( b <= a and b <= c ):
    result = b
else :
    result = c

print(result)