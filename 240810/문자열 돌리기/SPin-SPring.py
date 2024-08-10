str1 = input()
print(str1)
for i in range(len(str1)):
    str1 = str1[-1] + str1[:-1]
    print(str1)