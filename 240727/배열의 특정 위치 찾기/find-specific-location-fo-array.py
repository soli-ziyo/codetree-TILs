arr= list(map(int, input().split()))

sum=0

sum2 =0
mean =0
mylist =[] ; mylist2=[]

for i in range(10):
    if (i+1) %3 ==0:
        mylist.append(arr[i])
    if (i+1) %2 ==0:
        mylist2.append(arr[i])

k = len(mylist)
for j in mylist:
    sum2 +=j
for j in mylist2:
    sum +=j
mean = sum2/k
print(f"{sum} {mean:.1f}")