theSum = 0
nums = 0
data = input("Enter a number or hit enter to quit: ")
while data != "":
    number = float(data)
    theSum += number
    nums += 1
    data = input("Enter a number or hit enter to quit: ")
avg = theSum/nums
print(nums)
print("The sum is", theSum)
print("The average is ", avg)
