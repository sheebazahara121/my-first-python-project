print("*****student grade calculation*****")

name=input("enter a student name")

marks=float(input("enter marks(out of 100):"))

if marks>=90:
    print("grade=A+")
elif marks>=80:
    print(" grade=A")
elif marks>=70:
    print( "grade=B")
elif marks>=60:
    print(" grade=C")
elif marks>=50:
    print("grade=D")
else:
    grade="F"
    