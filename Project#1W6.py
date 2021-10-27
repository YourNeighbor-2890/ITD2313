word = input("Please input your plain text: ")
shift = int(input("Please input your shift: "))
code = ""
for ch in word:
    ordvalue = ord(ch)
    cipherValue = ordvalue + shift
    if cipherValue > ord('a') + shift - \
                     ord('z') - ordvalue + 1:
        code += chr(cipherValue)
print(code)
