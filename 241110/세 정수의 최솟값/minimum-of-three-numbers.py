inp = input()
arr = inp.split()
a, b, c = int(arr[0]), int(arr[1]), int(arr[2])

if ( a <= b and a <= c ):
    result = a
elif ( b <= a and b <= c ):
    result = b
else :
    result = c

print(result)