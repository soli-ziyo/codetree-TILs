arr = list(map(int, input().split()))
sum=0
mylist =[]

for i in range(10):
    if i+1 ==3 or i+1 ==5 or i+1 ==10:
        mylist.append(arr[i])

for j in mylist:
    sum +=j 

print(sum)