arr = list(map(int, input().split()))
num = len(arr)
mylist = [] ; mylist2=[]
for i in range(num):
    if i %2 ==0: #홀수번째 입력받은 정수
        mylist.append(arr[i])
    else:
        mylist2.append(arr[i])
sum=0; sum2=0
for j in mylist:
    sum += j
for j in mylist2:
    sum2 +=j

if sum >sum2:
    print(sum-sum2)
else:
    print(sum2-sum)