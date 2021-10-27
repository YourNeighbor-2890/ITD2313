sideOne = int(input("Please input the length of the first side: "))
sideTwo = int(input("Please input the length of the second side: "))
sideThree = int(input("Please input the length of the third side: "))

if sideOne == sideTwo and sideTwo == sideThree:
    print("This is an equilateral triangle")
else:
    print("This is not an equilateral triangle")
