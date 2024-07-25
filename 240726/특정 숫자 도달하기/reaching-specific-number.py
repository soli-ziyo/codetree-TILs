arr = list(map(int, input().split()))
cnt =0
mylist = []
sum =0
mean=0

for i in arr:
    if i <250:
        mylist.append(i)
    else:
        break

if len(mylist) ==0:
    n = len(arr)
    for j in range(n):
        sum += arr[j]
        mean = sum/n
else:
    n = len(mylist)
    for j in range(n):
        sum += mylist[j]
        mean = sum/n

print(f"{sum} {mean:.1f} ")