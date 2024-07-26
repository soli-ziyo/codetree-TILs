mylist = list(map(int, input().split()))
arr =[]

for i in mylist:
    if i !=0:
        if i %2 ==0:
            arr.append(i)
    else:
        break

k = len(arr)
sum =0

for i in arr:
    sum +=i 



print(f"{k} {sum}")