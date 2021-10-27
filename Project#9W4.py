sHeight = float(input("What is the starting height of the ball: "))
bHeight = float(sHeight *0.6)
bounces = float(input("How many times will the ball bounce: "))
totalDistance = float(sHeight)
i = int(0)

while i <= bounces:
    totalDistance = totalDistance + bHeight
    bHeight = bHeight *.6
    print(bHeight)
    print(i)
    i = i + 1
    if i == bounces:
        break
print(totalDistance)

