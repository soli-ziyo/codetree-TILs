str1 = input()
str2 = input()
cnt = 0

for i in range(len(str1)):
    if str1[i] == str2:
        cnt +=1

print(cnt)