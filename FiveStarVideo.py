daysNV = int(input("How many days has the new video been rented: "))
daysOV = int(input("How many days has the old video been rented: "))
totalNV = daysNV * 3
print(totalNV)
totalOV = daysOV * 2
print(totalOV)
total = totalOV + totalNV
print("The total is $", total)
