n = int(input())

arr = list(input().split())
str1 =""
for i in arr:
    str1 +=i
cnt =0
for j in range(len(str1)):
    print(str1[j], end='')
    cnt +=1
    if cnt % 5 ==0:
        print('')