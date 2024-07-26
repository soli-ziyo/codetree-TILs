arr = list(map(int, input().split()))
mylist =[]

for i in arr:
    if i !=0:
        mylist.append(i)
    else:
        break

k =len(mylist)
sum =0
for i in mylist:
    sum +=i

mean = sum /k

print(f"{sum} {mean:.1f}")