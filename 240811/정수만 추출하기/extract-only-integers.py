a, b = input().split()
list1 = list(a)
list2 = list(b)
str1 ="" ; str2 = ""

for i in list1:
    if i.isdigit():
        str1 +=i
    else:
        break

for j in list2:
    if j.isdigit():
        str2 +=j
    else:
        break

print(int(str1)+int(str2))