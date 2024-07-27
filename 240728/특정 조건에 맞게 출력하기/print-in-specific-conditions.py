arr = list(map(int, input().split()))
mylist =[]
for i in arr:
    if i ==0:
        break
    else:
        mylist.append(i)

for j in mylist:
    if j %2 ==0:
        print(j//2, end =' ')
    else:
        print(j+3, end=' ')