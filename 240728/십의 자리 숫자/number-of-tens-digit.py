arr = list(map(int, input().split()))
num = len(arr)
cnt =[0]*(num+1)

for i in arr:
    if i ==0:
        break
    else:
        cnt[i//10] +=1

for i in range(1,10):
    print(f"{i} - {cnt[i]}")