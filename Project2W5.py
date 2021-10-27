sideOne = int(input("Please input the length of the first side: "))
sideTwo = int(input("Please input the length of the second side: "))
sideThree = int(input("Please input the length of the long side: "))

if sideOne **2 + sideTwo **2 == sideThree **2: 
    print("This is a right triangle")
else:
    print("This is not a right triangle")
