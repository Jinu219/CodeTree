firstperson = input().split(" ")
secondperson = input().split(" ")
thirdperson = input().split(" ")

result = 0

if(firstperson[0] == 'Y' and int(firstperson[1]) >= 37):
    result += 1
if(secondperson[0] == 'Y' and int(secondperson[1]) >= 37):
    result += 1
if(thirdperson[0] == 'Y' and int(thirdperson[1]) >= 37):
    result += 1

if(result >= 2 ):
    print("E")
else :
    print("N")