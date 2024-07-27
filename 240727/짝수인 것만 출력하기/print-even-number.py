n = int(input())

arr = list(map(int, input().split()))
mylist =[]

for i in arr:
    if i %2 ==0:
        mylist.append(i)

for j in mylist:
    print(j, end=' ')