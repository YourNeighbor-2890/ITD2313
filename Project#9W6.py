name = input("please input your last name: ")
filename = name + str(".txt")
print(filename)
wage = int(input("Please input what you make per hour: "))
hours = int(input("Please inout how many hours you worked this week: "))
totalpay = wage * hours
f = open(filename, 'w')
f.write(name + " per hour " + str(wage) + " hours: " + str(hours) + " total pay: " + str(totalpay))
f.close()

