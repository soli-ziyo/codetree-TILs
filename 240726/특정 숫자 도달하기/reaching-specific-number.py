arr = list(map(int, input().split()))
cnt =0
mylist = []
sum =0

for i in arr:
    if i <250:
        mylist.append(i)
    else:
        n = len(mylist)
        if n !=0:
            for j in range(n):
                sum += mylist[j]
            break
        else:
            n = len(arr)
            for j in range(n):
                sum += arr[j]
            break

print(f"{sum} {sum/n:.1f}")