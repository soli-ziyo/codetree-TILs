arr = list(map(int, input().split()))
mylist =[]
for i in arr:
    if i %3 ==0:
        break
    else:
        mylist.append(i)

print(mylist[-1])