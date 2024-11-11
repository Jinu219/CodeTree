a_math, a_eng = input().split(" ")
b_math, b_eng = input().split(" ")

a_math = int(a_math)
a_eng = int(a_eng)

b_math = int(b_math)
b_eng = int(b_eng)

if(a_math > b_math or (a_math == b_math and a_eng > b_eng)):
    print("A")
else :
    print("B")