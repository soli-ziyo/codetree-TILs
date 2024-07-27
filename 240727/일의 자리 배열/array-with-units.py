arr = list(map(int, input().split()))
mylist =[] ; mylist2=[]

for i in range(10):
    arr.append(arr[-1]+arr[-2])

for j in range(10):
    mylist.append(arr[j])

for i in mylist:
    print(i%10, end=' ')