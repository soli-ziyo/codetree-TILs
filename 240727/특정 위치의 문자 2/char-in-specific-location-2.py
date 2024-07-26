mylist = list(input().split())
arr =[]
k = len(mylist)
for i in range(k):
    if (i+1) ==2 or (i+1) ==5 or (i+1)==8:
        arr.append(mylist[i])

for i in arr:
    print(i, end=' ')