cnt = 0
str_list = []
while True:
    str1 =input()
    if str1 =="0":
        break
    else:
        cnt +=1 
        if cnt %2 !=0:
            str_list.append(str1)
        else:
            continue

print(cnt)
for j in str_list:
    print(j)