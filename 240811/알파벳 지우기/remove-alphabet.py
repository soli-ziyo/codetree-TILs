str1 = input() ; str2 = input()
list1 = list(str1) ; list2 = list(str2)
a = "" ; b = ""
for i in list1:
    if i.isdigit():
        a += i 
for j in list2:
    if j.isdigit():
        b += j 
print(int(a)+int(b))