firstEye = float(input())
secondEye = float(input())

if (firstEye >= 1.0 and secondEye >= 1.0) :
    print("High")
elif(firstEye >= 1.0 and secondEye >= 0.5):
    print("Middle")
elif(firstEye >= 0.5 and secondEye >= 1.0):
    print("Middle")
elif(firstEye >= 0.5 and secondEye >= 0.5):
    print("Middle")
else :
    print("Low")