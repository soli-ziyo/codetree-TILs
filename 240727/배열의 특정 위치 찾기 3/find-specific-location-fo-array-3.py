arr = list(map(int, input().split()))
mylist =[]
for i in arr:
    if i !=0:
        mylist.append(i)
    else:
        break

sum = mylist[-1]+mylist[-2]+mylist[-3]

print(sum)