a = int(input().end="")
b = int(input().end="")
c = int(input().end="")


if ( a <= b and a <= c ):
    result = a
elif ( b <= a and b <= c ):
    result = b
else :
    result = c

print(result)